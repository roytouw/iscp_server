import codecs
import json
import os


class SavedTweetLoader:

    def __init__(self):
        self.local_tweets = self.load_tweets()

    def load_tweets(self):
        dir = os.path.dirname(__file__)
        filename = os.path.join(dir, '../tweetlist.json')
        return set(codecs.open(filename, "r", "utf-8").read().split())

    def get_tweets(self):
        result = []
        for tweet in self.local_tweets:
            result.append(tweet.split(" "))
        return result

    def reload(self):
        self.local_tweets = self.load_tweets()
