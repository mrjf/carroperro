#!/usr/bin/env python
"""Test behavior of cars module"""

__author__ = "Russell Horton"
__copyright__ = "Copyright 2018, All Rights Reserved"
__license__ = "For Toptal candidacy evaluation only. No license is granted."
__version__ = "0.1"
__maintainer__ = "Russell Horton"
__email__ = "russ@bagaduce.com"

import unittest

from carroperro.cars import Cars


class CarsTest(unittest.TestCase):

    cars = Cars()

    def test_data(self):

        self.assertEqual(len(Cars.makes_models), 291)
        self.assertEqual(len(self.cars.makes_models), 291)
        self.assertEqual(len(self.cars.makes_models), 291)

    def test_hashtags(self):

        self.assertEqual(len(self.cars.make_model_hashtags), 291)
        self.assertEqual(
            self.cars.make_model_hashtags['toyotalandcruiser'],
            ('Toyota', 'Land Cruiser'),
        )
        self.assertEqual(
            self.cars.model_hashtags['landcruiser'],
            ('Toyota', 'Land Cruiser'),
        )
        self.assertEqual(
            self.cars.model_hashtags['mx5miata'],
            ('Mazda', 'MX-5 Miata'),
        )

    def test_name_from_hashtag(self):
        self.assertEqual(
            self.cars.name_from_hashtag('toyotayaris'), 'Toyota Yaris',
        )


if __name__ == '__main__':
    unittest.main()
