class LongestWord:
    """
    Finds all the path between nodes
    """

    def longest_word(self, words):
        if len(words) == 0:
            return None
        _words = sorted(words, key=lambda word: (-len(word), word))
        for word in _words:
            if all(word[:len(word) - i] in _words for i in range(len(word))):
                return word
        return ""



lw = LongestWord()
words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
print("longest word is: {}".format(lw.longest_word(words)))
