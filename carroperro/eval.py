#!/usr/bin/env python
"""Test the performance of the ALS car-dog recommender

See https://gist.github.com/bwhite/3726239 for (n)dcg inspiration."""

from scipy import stats
import numpy
from carroperro import counting


class Eval(object):

    def __init__(self, als):
        """
        Args:
            als (ALS): the ALS model
        """
        self.als = als

    @staticmethod
    def dcg_at_k(scores, k):
        """Distributed cumulative gain

        Args:
            scores (list): of floats, the scores to be evaluated
            k (int): the number of top scores to be considered

        Returns:
            float: the ndcg score
        """
        scores = scores[:k]
        return scores[0] + numpy.sum(scores[1:] /
                                     numpy.log2(
                                         numpy.arange(2, len(scores) + 1),
                                     ))

    @staticmethod
    def ndcg_at_k(scores, k=5):
        """Normalized distributed cumulative gain

        Args:
            scores (list): of floats, the scores to be evaluated
            k (int): the number of top scores to be considered

        Returns:
            float: the ndcg score
        """
        max_dcg = Eval.dcg_at_k(sorted(scores, reverse=True), k)
        if max_dcg == 0:
            return 0.0
        else:
            return Eval.dcg_at_k(scores, k) / max_dcg

    def recommend_cars_baseline(self):
        """A baseline recommender that always recommends the 5 best-selling
        cars in America with arbitrary scores in descending order of
        popularity.

        Returns:
            list: of 2-tuples, (car: str, score: float)
        """

        top_cars = [
            ('Hyundai Elantra', 1.5),
            ('Chevrolet Cruze', 1.2),
            ('Ford Fusion', 0.9),
            ('Nissan Sentra', 0.6),
            ('Nissan Altima', 0.3),
        ]

        return [
            {'car': self.als.car_lookup[car], 'score': score}
            for car, score in top_cars
        ]

    def eval(self, alpha=0.005):
        """Calculate NDCG for the baseline method and ALS for recommending
        the top 5 cars for all dogs. Report the mean average NDCG of each
        type. Perform a t-test on the two lists of NDCG scores and report the
        p-value. A very low p-value (>>0.05) indicates we can reject the
        null-hypothesis that both recommender methods have the same true
        average scores and that variation between their reported scores is
        due to random variation in the samples.

        Returns:
            float: the p-value of the t-test
        """

        dog_oriented_counts = counting.reverse_counts(self.als.counts)

        baseline_ndcgs = []
        als_ndcgs = []
        baseline_better = 0
        als_better = 0
        same_ndcg = 0

        for dog_id, car_counts in dog_oriented_counts.items():
            baseline_scores = [dog_oriented_counts[dog_id].get(
                self.als.car_lookup[rec['car']], 0,
            )
                for rec in self.recommend_cars_baseline()]

            als_scores = [dog_oriented_counts[dog_id].get(
                self.als.car_lookup[rec['car']], 0,
            )
                for rec in self.als.recommend_cars(
                    [self.als.dog_lookup[dog_id]], k=5,
                )]

            baseline_ndcg = self.ndcg_at_k(baseline_scores, k=5)
            als_ndcg = self.ndcg_at_k(als_scores, k=5)
            baseline_ndcgs.append(baseline_ndcg)
            als_ndcgs.append(als_ndcg)

            if baseline_ndcg > als_ndcg:
                baseline_better += 1
            elif als_ndcg > baseline_ndcg:
                als_better += 1
            else:
                same_ndcg += 1

        mean_baseline_ndcg = numpy.mean(baseline_ndcgs)
        mean_als_ndcg = numpy.mean(als_ndcgs)
        tstat, pval = stats.ttest_ind(baseline_ndcgs, als_ndcgs)
        if pval < alpha:
            accept = "can"
        else:
            accept = "can't"

        report = """Calculated NDCG on car recommendations for %d dogs.
The mean average NDCG for the baseline method was %.5f, compared with
%.5f for the ALS method. In %d cases, the baseline recommender outperformed
ALS, while ALS had a higher NDCG in %d cases (%d cases were a tie).

A t-test indicated a p-value of %.35f. Using a threshold of %s, we %s
reject the null hypothesis and conclude that there is a
significant difference between the baseline and ALS recommender performance."""
        filled_report = report % (
            len(dog_oriented_counts.keys()), mean_baseline_ndcg, mean_als_ndcg,
            baseline_better, als_better, same_ndcg, pval, alpha, accept,
        )

        print(filled_report)
        return pval
