#!/usr/bin/env python
"""Test behavior of counting module"""

__author__ = "Russell Horton"
__copyright__ = "Copyright 2018, All Rights Reserved"
__license__ = "For Toptal candidacy evaluation only. No license is granted."
__version__ = "0.1"
__maintainer__ = "Russell Horton"
__email__ = "russ@bagaduce.com"

import unittest
from carroperro import counting


class UtilTest(unittest.TestCase):

    def test_reverse_counts(self):

        counts = {
            'prius': {'lab': 1, 'mutt': 3},
            'yaris': {'lab': 4, 'pittie': 2},
            'golf': {'golden': 4, 'pittie': 1},
        }
        reversed_counts = {
            'lab': {'prius': 1, 'yaris': 4},
            'mutt': {'prius': 3},
            'pittie': {'yaris': 2, 'golf': 1},
            'golden': {'golf': 4},
        }

        self.assertEqual(reversed_counts, counting.reverse_counts(counts))


if __name__ == '__main__':
    unittest.main()
