"""Perform ALS collaborative filtering on the cars/dogs dataset."""

	
from collections import defaultdict
import numpy
import scipy
from implicit.als import AlternatingLeastSquares
from carroperro import util
from carroperro.cars import Cars
from carroperro.dogs import Dogs
from carroperro import counting


class ALS(object):
    """Builds ALS model from coocurrence data

    Attributes:
        cars (Cars): car names and hastags
        dogs (Dogs): dog names and hastags
        counts: dict of dict showing coocurrence counts
        car_lookup (dict): mapping from ids to car names and vice versa
        dog_lookup (dict): mapping from ids to dog names and vice versa
    """

    def __init__(self, cooc_path):
        """
        Args:
            cooc_path (str): the path for the CSV coocurrence count file
        """
        self.cars = Cars()
        self.dogs = Dogs()
        self.counts = None
        self.car_lookup = None
        self.dog_lookup = None
        self.matrix = None
        self.model = None

        self.counts = counting.read_count_csv(cooc_path)
        self.lookups_from_counts()
        self.matrix_from_counts()
        self.model_from_matrix(5)

    def recommend_cars(self, dog_ids, k=5):
        """Recommend cars for a user whose profile is comprised of a list of
        dog ids that user has expressed a liking for. Recommendations are a
        achieved by finding the top cars for each dog, summing their scores,
        and returning the top n cars from that scored collection.

        Args:
            dog_ids (list): of int, the dogs the user likes
            n (int): the number of cars to recommend

        Returns:
            list: of 2-tuples, (car: str, score: float)
        """

        scored_cars = defaultdict(float)

        for dog_id in dog_ids:
            for car_id, score in self.model.recommend(
                    dog_id, self.matrix.tocsr(),
            ):
                scored_cars[car_id] += score

        sorted_cars = sorted(
            scored_cars.items(), key=lambda x: x[1],
            reverse=True,
        )
        normalized_cars = [
            {
                'car': int(car_id),
                'score': float(score) / len(dog_ids),
            }
            for car_id, score in sorted_cars
        ]

        return normalized_cars[:k]

    def name_from_hashtag(self, hashtag):
        """Find the full canonical name for a car or a dog from its hashtag.

        Note this is not safe if car and dog hashtags can collide (e.g.
        if there is a car model that is the same string as a dog breed), but
        this is not the case in the data used.

        Args:
            hashtag: string, the hastag (without #)

        Returns:
            string: either 'car', or 'dog', depending on which type was found
            string: the name recovered

        Raises:
            ValueError: if there is neither a dog nor a car matching that
                hashtag
        """
        car_name = self.cars.name_from_hashtag(hashtag)
        if car_name:
            return 'car', car_name
        dog_name = self.dogs.name_from_hashtag(hashtag)
        if dog_name:
            return 'dog', dog_name
        raise ValueError('No name found for hashtag: ' + hashtag)

    def lookups_from_counts(self):
        """Build bi-directional lookup tables from car/dog names -> ids and
        ids -> car/dog names, using all cars and dogs in the counts.
        """

        cars = self.counts.keys()
        self.car_lookup = util.two_way_index(sorted(cars))

        dogs = list(set(
            [dog for dog_counts in self.counts.values() for dog in dog_counts],
        ))
        self.dog_lookup = util.two_way_index(sorted(dogs))

    def matrix_from_counts(self):
        """Build a scipy.sparse.coo_matrix from the counts"""

        cars = []
        dogs = []
        counts = []

        for car, dog_counts in self.counts.items():
            for dog, count in dog_counts.items():
                cars.append(self.car_lookup[car])
                dogs.append(self.dog_lookup[dog])
                counts.append(count)

        row = numpy.array(cars)
        col = numpy.array(dogs)
        data = numpy.array(counts)

        self.matrix = scipy.sparse.coo_matrix((data, (row, col)))

    def model_from_matrix(self, factors):
        """Fit an ALS model on the matrix

        Args:
            factors (int): the number of latent factors to use
        """

        self.model = AlternatingLeastSquares(
            factors=factors, dtype=numpy.float32,
            use_gpu=False,
        )
        self.model.fit(self.matrix)
