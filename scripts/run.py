#!/usr/bin/env python
"""Run the ALS webservice"""

from carroperro.als import ALS
from carroperro.server import Server

als = ALS('data/hashtag_counts.csv')

server = Server(als)
server.run()
