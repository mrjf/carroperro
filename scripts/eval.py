#!/usr/bin/env python
"""Run the NDCG evaluation of the ALS recommender"""

from carroperro.als import ALS
from carroperro.eval import Eval

als = ALS('data/hashtag_counts.csv')

eval = Eval(als)
eval.eval()
