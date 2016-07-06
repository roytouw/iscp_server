import os

class DataAnalyzer:
    #list_location = "twitter_sentiment_list.csv"
    dir = os.path.dirname(__file__)
    list_location = os.path.join(dir, '../twitter_sentiment_list.csv')

    def __init__(self):
        self.sentiment_list = self.read_sentiment_list()

    # Read the words with the sentimental values.
    def read_sentiment_list(self):
        sentiment_list = open(self.list_location, 'r')
        words = {}
        for line in sentiment_list:
            line = line.replace(";", "")
            line = line.replace("\"", "")
            tokens = line[:-1].split(',')
            words[tokens[0]] = (tokens[1], tokens[2])
        return words

    def analyze_tweet(self, tweet):
        happy_value, sad_value = 0, 0
        for tweet_word in tweet:
            for word, value in self.sentiment_list.items():
                try:
                    if tweet_word == word:
                        happy_value += float(value[0])
                        sad_value += float(value[1])
                except ValueError as ex:
                    print(ex)
                    continue  # If the word can't be compared, skip it.
        combined_result = (happy_value, sad_value)
        return combined_result

    def analyze_result(self, result_set):
        positive, negative = 0, 0
        for i in result_set:
                positive += i[0]
                negative += i[1]
        result = (positive, negative)
        return result

    def analyze_tweet_list(self, tweets):
        result_set = []
        for tweet in tweets:
            result_set.append(self.analyze_tweet(tweet))
        return self.analyze_result(result_set)
