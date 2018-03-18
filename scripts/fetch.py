#!/usr/bin/env python
"""Generate all the hastags from cars and dogs.
Search Twitter for each of the hastags and find all users who use that hashtag.
Search in each of those users timelines to count all their uses of all of the
hastags. Save these coocurrence counts in once file for each hashtag.

This process can take a very long time, depending on how many user timelines
you fetch for each hashtag use. Defaults to 25, at which level it may take
24 - 48 hours to run completely.
"""
# from __future__ import absolute_import

	
from carroperro.dogs import Dogs
from carroperro.cars import Cars
from carroperro.cormorant import Cormorant
from carroperro import counting

dogs = Dogs()
cars = Cars()

all_hashtags = list(cars.model_hashtags.keys()) +\
    list(cars.make_model_hashtags.keys()) +\
    list(dogs.breed_hashtags.keys())

cormorant = Cormorant.from_app_conf()

cormorant.save_all_hashtag_coocs(
    all_hashtags, 'data/hashtag_coocs',
    user_limit=25,
)

counts = counting.build_counts_from_coocs('data/hashtag_coocs', cars, dogs)
counting.write_counts_csv(counts, 'data/hashtag_counts.csv')
