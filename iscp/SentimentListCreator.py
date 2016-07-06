import json

from Word import Word


class SentimentListCreator:

    def __init__(self, mood, *keywords):
        if mood is "positive":
            self.positive = True
        elif mood is "negative":
            self.positive = False
        else:
            raise ValueError('Only "positive" and "negative" sentiment lists can be created')
        self.words = self.load_lexicon()
        self.keywords = keywords

    def shout_words(self):
        for word in self.words:
            print(word.get_word(), " : ", word.get_pos(), "   ", word.get_neg())

    """
        Check if word already registered,
        if not registered, return True
        if registered, adjust sentimental value, return False
    """
    def check_new_word(self, word):
        for i in self.words:
            if i.get_word() == word:
                if self.positive:
                    i.raise_positive(1)
                else:
                    i.raise_negative(1)
                return False
        return True

    def set_mood(self, mood):
        if mood == "positive":
            self.Positive = True
        elif mood == "negative":
            self.Positive = False
        else:
            raise ValueError("Only positive and negative moods allowed!")

    def add_word(self, word):
        word = word.replace(",", "").lower()
        if self.check_new_word(word):
            word = Word(word, 0, 0)
            self.words.append(word)

    def save_lexicon(self):
        filename = ""
        for i in self.keywords:
            filename += i
        data = []
        for i in self.words:
            line = i.get_word() + "," + str(i.get_pos()) + "," + str(i.get_neg())
            data.append(line)
        with open("lexicon.json", 'w') as fp:
            json.dump(data, fp)

    def load_lexicon(self):
        lexicon = []
        try:
            with open("lexicon.json", "r") as fp:
                tmp_list = json.load(fp)
                for i in tmp_list:
                    i = i.split(",")
                    try:
                        lexicon.append(Word(i[0], i[1], i[2]))
                    except ValueError as exception:
                        print(exception)
                        continue
                return lexicon
        except FileNotFoundError:
            print("No lexicon was found, starting with empty one")
            return lexicon

    def remove_single_instances(self):
        new_list = []
        for word in self.words:
            if word.get_neg() + word.get_pos() > 0:
                new_list.append(word)
        self.words = new_list

    def sort_lexicon(self):
        self.words = sorted(self.words, key=lambda word: word.get_total(), reverse=True)

    # Creates a sentiment list, from a list of tweets
    def create_sentiment_list(self, tweets):
        for tweet in tweets:
            for word in tweet:
                self.add_word(word)
        self.sort_lexicon()
        self.remove_single_instances()
        self.shout_words()
        self.save_lexicon()
