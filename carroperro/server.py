from collections import defaultdict

from flask import Flask
from flask import jsonify
from flask import request
from flask_api import status
from flask_restful import Api
from flask_restful import Resource

# Use a database in a real app
users = defaultdict(lambda: defaultdict(int))


class Server(object):

    def __init__(self, als):
        """Server for carroperro recommender system

        Args:
            port (int): the port to serve on
        """

        self.als = als
        self.app = Flask(__name__)
        api = Api(self.app)

        api.add_resource(
            AddData, '/addData/<user_id>/<dog_id>',
            resource_class_kwargs={'als': als},
        )

        api.add_resource(
            PredictInterests, '/predictInterests/<user_id>',
            resource_class_kwargs={'als': als},
        )

    def run(self, port=5002):
        """Start the server"""
        self.app.run(port=port)


class AddData(Resource):

    def __init__(self, als):
        self.als = als

    # In a real app, I'd make this a POST, but for ease of playing around in
    # the browser, here it's a GET operation
    def get(self, user_id, dog_id):
        """Add a data point to the in-memory user data store, indicating that
        the user likes a particular dog

        Args:
            user_id (str): the id of the user
            dog_id (str): the id of the dog
        """
        dog_id = int(dog_id)
        dog = self.als.dog_lookup.get(dog_id, None)
        if not dog:
            return str(dog_id) + ' not found in dogs lookup', \
                status.HTTP_400_BAD_REQUEST
        else:
            users[int(user_id)][dog_id] += 1
            print(users)
            return dog + ' added to user ' + user_id, \
                status.HTTP_200_OK


class PredictInterests(Resource):

    def __init__(self, als):
        self.als = als

    def get(self, user_id):
        """Predict the cars that a user might be interested in, based on the
        dogs they like.

        Args:
            user_id (str): the id of the user
        """

        if int(user_id) not in users:
            return user_id + ' not found in users', \
                status.HTTP_400_BAD_REQUEST

        dog_ids = list(users[int(user_id)].keys())
        print('dog_ids', dog_ids)
        predictions = self.als.recommend_cars(dog_ids, 5)

        if request.args.get('names'):
            predictions = [
                {
                    'car': self.als.car_lookup[prediction['car']],
                    'score': prediction['score'],
                }
                for prediction in predictions
            ]

        return jsonify(predictions)


if __name__ == '__main__':

    server = Server()
    server.run()
