#!/usr/bin/env python
"""Test behavior of dogs module"""

__author__ = "Russell Horton"
__copyright__ = "Copyright 2018, All Rights Reserved"
__license__ = "For Toptal candidacy evaluation only. No license is granted."
__version__ = "0.1"
__maintainer__ = "Russell Horton"
__email__ = "russ@bagaduce.com"

import unittest

from carroperro.dogs import Dogs


class DogsTest(unittest.TestCase):

    dogs = Dogs()

    def test_data(self):

        self.assertEqual(len(Dogs.breeds.keys()), 64)
        self.assertEqual(len(Dogs.breeds['Labrador Retriever']), 3)
        self.assertEqual(len(self.dogs.breeds), 64)

    def test_hashtags(self):

        self.assertEqual(len(self.dogs.breed_hashtags), 192)
        self.assertEqual(
            self.dogs.breed_hashtags['weimaraner'],
            'Weimaraner',
        )
        self.assertEqual(
            self.dogs.breed_hashtags['labradorretriever'],
            'Labrador Retriever',
        )
        self.assertEqual(
            self.dogs.breed_hashtags['chinesesharpei'],
            'Chinese Shar-Pei',
        )
        self.assertEqual(
            self.dogs.breed_hashtags['blacklab'],
            'Labrador Retriever',
        )
        self.assertEqual(
            self.dogs.breed_hashtags['rottie'],
            'Rottweiler',
        )
        self.assertEqual(
            self.dogs.breed_hashtags['rottweiler'],
            'Rottweiler',
        )
        self.assertEqual(
            self.dogs.breed_hashtags['rottweiler'],
            'Rottweiler',
        )

    def test_name_from_hashtag(self):
        self.assertEqual(
            self.dogs.name_from_hashtag('blacklab'), 'Labrador Retriever',
        )


if __name__ == '__main__':
    unittest.main()
