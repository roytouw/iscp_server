"""
 Author: Roy
 Date: 3-2-2016
 Project: TwitterDing
 Python Version: 3.4
"""
import threading

import time

from iscp.DataAnalyzer import DataAnalyzer
from iscp import SavedTweetLoader, TweetFetcher
import math


class TweetController:

    def __init__(self):
        self.tweetFetcher = TweetFetcher.TweetFetcher()
        self.savedTweetLoader = SavedTweetLoader.SavedTweetLoader()
        self.dataAnalyzer = DataAnalyzer()
        self.fetch_thread = threading.Thread(target=self.tweetFetcher.search)
        self.update_data = threading.Thread(target=self.update_data)
        self.last_results = []

    def update_data(self):
        while True:
            self.savedTweetLoader.reload()
            self.last_results.append(
                self.dataAnalyzer.analyze_tweet_list(self.savedTweetLoader.get_tweets())
            )
            print(self.last_results[-1])
            time.sleep(5)

    def start_drawing(self):
        self.update_data.start()

    def get_sentiment(self):
        self.savedTweetLoader.reload()
        current_tweets = self.savedTweetLoader.get_tweets()
        result_set = self.dataAnalyzer.analyze_tweet_list(current_tweets)
        sentiment_set = []
        for i in result_set:
            sentiment_set.append(i)
        return self.translate_for_graph(sentiment_set)

    def translate_for_graph(self, sentiment_set):
        sentiment_set[0] = math.fabs(sentiment_set[0])
        sentiment_set[1] = math.fabs(sentiment_set[1])
        sentiment_set.insert(0, (sentiment_set[0] + sentiment_set[1]))
        return sentiment_set

    def search_tweets(self, tweet):
        try:
            self.tweetFetcher.set_search_terms(tweet)
            self.fetch_thread.start()

        except:
            print("Error thrown starting new thread")
