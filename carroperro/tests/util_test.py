#!/usr/bin/env python
"""Test behavior of dogs module"""

__author__ = "Russell Horton"
__copyright__ = "Copyright 2018, All Rights Reserved"
__license__ = "For Toptal candidacy evaluation only. No license is granted."
__version__ = "0.1"
__maintainer__ = "Russell Horton"
__email__ = "russ@bagaduce.com"

import unittest
from carroperro import util
from carroperro.cars import Cars
from carroperro.dogs import Dogs


class UtilTest(unittest.TestCase):

    def test_find_hashtags(self):

        text = 'I wanted to #wash my #hands #soclean22'
        hashtags = util.find_hashtags(text)
        self.assertEqual(hashtags, ['wash', 'hands', 'soclean22'])

    def test_fold_hashtag(self):
        self.assertEqual(
            util.fold_hashtag('ABC-123'),
            util.fold_hashtag('abc_123'),
        )

    def test_name_from_hashtag(self):
        cars = Cars()
        dogs = Dogs()

        self.assertEqual(
            util.name_from_hashtag(
                'toyotalandcruiser', cars, dogs,
            ), ('car', 'Toyota Land Cruiser'),
        )

        self.assertEqual(
            util.name_from_hashtag(
                'yaris', cars, dogs,
            ), ('car', 'Toyota Yaris'),
        )

        self.assertEqual(
            util.name_from_hashtag(
                'pugs', cars, dogs,
            ), ('dog', 'Pug'),
        )

        self.assertEqual(
            util.name_from_hashtag(
                'ducktollingretrievers', cars, dogs,
            ),
            ('dog', 'Nova Scotia Duck Tolling Retriever'),
        )

    def test_two_way_index(self):

        items = ['foo', 'bar', 'zap', 'something else']

        lookup = util.two_way_index(items)

        self.assertEqual(lookup['foo'], 0)
        self.assertEqual(lookup[0], 'foo')
        self.assertEqual(lookup[3], 'something else')
        self.assertEqual(lookup['something else'], 3)


if __name__ == '__main__':
    unittest.main()
