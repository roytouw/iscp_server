import codecs

import time
from TwitterSearch import TwitterSearchOrder
from TwitterSearch import TwitterSearchException
from TwitterSearch import TwitterSearch
import json
import os


class TweetFetcher:

    def __init__(self, *search_terms):
        self.search_terms = [search_terms]
        self.data = []
        dir = os.path.dirname(__file__)
        self.tweet_list = os.path.join(dir, '../tweetlist.json')

    def set_search_terms(self, *search_terms):
        self.search_terms = [search_terms]

    def get_current_data(self):
        return self.data

    def save_data(self, tweets_to_save):
        try:
            with open(self.tweet_list, 'w') as fp:
                json.dump(tweets_to_save, fp)
        except FileNotFoundError as exception:
            print(exception)

    def save_line(self, line):

        file = codecs.open(self.tweet_list, "a", "utf-8")
        file.write(line)
        file.close()
        time.sleep(1)

    def search(self):
        try:
            tso = TwitterSearchOrder()
            tso.set_keywords(*self.search_terms)
            tso.set_include_entities(False)
            tso.set_count(100)

            ts = TwitterSearch(
                consumer_key='aOUVcCWLIYEbUvHW5dLjVc7Gf',
                consumer_secret='8qb3LTAHbj43J40Rxm0RMLAOaP4QoEHfFVGTeJ3S6iUmSBq6JJ',
                access_token='4251433696-ulZx8dJ3QZE95ds0PhXNldeKFhjhBUoGSuGycSE',
                access_token_secret='wx65NQaBHHgwC4xLOgRxFSs4kWWzkg09KkgNkAKHZryks'
            )

            for tweet in ts.search_tweets_iterable(tso):
                self.data.append(tweet['text'])
                self.save_line(tweet['text'])

            # self.save_data(self.data)
        except TwitterSearchException as exception:
            print(exception)
