#!/usr/bin/env python
"""Twitter API functions using Tweepy library, to fetch and store results.
Since it's Twitter-related, the class is named after a bird."""	

import os
from collections import Counter
import json
import configparser
import tweepy
from carroperro import util


class Cormorant:

    def __init__(self, tweepy_api):

        self.tweepy_api = tweepy_api

    @classmethod
    def from_app_conf(cls, app_conf_path='/usr/local/etc/cormorant.ini'):
        """Build the Tweepy API from app conf keys stored in a local conf
        file

        Args:
            app_conf_path (str): location of the conf file containing Twitter
                API secrets

        Returns:
            Cormorant: instance of this class instantiated with a Tweepy API
        """

        config = configparser.RawConfigParser()
        config.read(os.getenv('CORMORANT_INI', app_conf_path))

        return cls.from_app_keys(
            config.get('twitter', 'consumer_key'),
            config.get('twitter', 'consumer_secret'),
        )

    @classmethod
    def from_app_keys(cls, consumer_key, consumer_secret):
        """Build the Tweepy API from the app keys (uses app API rate limits
        instead of lower account limits, can't perform account actions)

        Args:
            consumer_key (str): Twitter API consumer key
            consumer_secret (str): Twitter API consumer secret

        Returns:
            Cormorant: instance of this class instantiated with a Tweepy API
        """

        auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)

        api = tweepy.API(
            auth, wait_on_rate_limit=True,
            wait_on_rate_limit_notify=True,
        )

        return cls(api)

    def get_all_users_in_search(self, query):
        """Return a set of all users who have posted a status matching a given
        query

        Args:
            query: the query to search Twitter for

        Returns:
            list: of ints, the user ids who have tweets matching the query
        """

        users = set()

        for tweet in tweepy.Cursor(
            self.tweepy_api.search,
            q=query,
            count=100,
        ).items():
            users.add(tweet.user.id)

        return users

    def get_hashtag_mentions_in_users_timeline(self, users, hashtags):
        """Get user timelines and count all hashtag occurrences in them.
        Multiple occurrences of the same hashtag in a single tweet count only
        once.

        Args:
            users (list(str)): the user ids whose timelines should be fetched
                and searched for the hashtags
            hashtags (list(str)): the hashtags to search for in user timelines


        Returns:
            Counter: the count of the hashtags in all users timelines.
        """

        mentions = []

        i = 0

        for user in users:
            i += 1
            print(i, 'of', len(users), 'user', user)
            for tweet in tweepy.Cursor(
                self.tweepy_api.user_timeline,
                id=user,
                count=200,
            ).items():
                folded_tweet = tweet.text.lower()
                tweet_hashtags = set(util.find_hashtags(folded_tweet))
                found_hashtags = tweet_hashtags.intersection(hashtags)
                mentions += list(found_hashtags)

        return Counter(mentions)

    def save_user_hashtag_counts(self, users, hashtags, path):
        """Save a dictionary containing counts of the number of tweets that
        contain each hashtag in any of the given users timelines

        Args:
            users (list(str)): the user ids whose timelines should be fetched
                and searched for the hashtags
            hashtags (list(str)): the hashtags to search for in user timelines
            path (str): the path to which to save the hashtag coocurrence data
        """

        hashtag_counts = self.get_hashtag_mentions_in_users_timeline(
            users,
            hashtags,
        )

        with open(path, 'w') as f:
            f.write(json.dumps(hashtag_counts))

    def save_all_hashtag_coocs(self, hashtags, path, user_limit=25):
        """For every hashtag, find up to user_limit users that have used that
        hashtag, and for each such user, find any other uses of a hashtag in
        the supplied list, and save the counts of the hashtag-hashtag
        coocurrences to a file.


        Args:
            hashtags (list(str)): the hashtags to search for
            path (str): the path to which to save the hashtag coocurrence data
            user_limit (int): the maximum number of users to process. Because
                processing a user involves fetching their entire timeline,
                this is expensive in time and API calls. A higher limit results
                in more data but longer runtime.
        """

        # TODO add logging
        # TODO need to catch occasional 500, 504 errors from Twitter and retry

        i = 0
        for hashtag in hashtags:
            i += 1
            users = list(self.get_all_users_in_search('#' + hashtag))
            self.save_user_hashtag_counts(
                users[:user_limit], hashtags, path + '/' + hashtag,
            )
