class Trie:
    TERMINAL = '*'

    def __init__(self):
        self.head = {}
        self._longest_word = ""


    # @param {string} word
    # Return void
    # Inserts a word in the trie
    def add(self, word):
        self.check_for_longest(word)
        node = self.head
        for letter in word:
            if letter not in node:
                node[letter] = {}
            node = node[letter]
        node[Trie.TERMINAL] = True

    # @param {string} prefix
    # Return {boolean}
    # returns true if prefix exists in dictionary
    def search_word(self, word):
        """
        Returns True if prefix exists
        """
        node = self.head
        for letter in word:
            if  letter not in node:
                return False
            node = node[letter]
        return trie.TERMINAL in node

    def longest_word(self):
        return self._longest_word

    def check_for_longest(self, word):
        if len(self._longest_word) < len(word):
            self._longest_word = word

trie = Trie()
trie.add("bull")
trie.add('buy')
trie.add('bid')
trie.add('bell')
trie.add('bar')
trie.add('sell')
trie.add('stock')
trie.add('stop')
trie.add('sto')
print(trie.search_word("stock"))
print("longest word: {}".format(trie.longest_word()))
