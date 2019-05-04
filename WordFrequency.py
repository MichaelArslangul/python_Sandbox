from collections import defaultdict


class Frequency:

    def __init__(self, text):
        self.text = text
        self._word = []
        self._d_word = defaultdict(int)

    def tokenize_text(self):
        self._word = self.text.split()

    def construct_word_count(self):
        self.tokenize_text()
        for _word in self._word:
            self._d_word[_word] += 1

    def count_occurences(self, word):
        self.construct_word_count()
        return self._d_word[word]


text = "This is a string with lots of words and string and stuff which \
continues and continues until I am tired of typing. Cette phrase est meme \
en 2 langues. On n'en finit plus"
freq = Frequency(text)
print("frequency of word: {} is: {}".format(
    "and", freq.count_occurences("and")))
