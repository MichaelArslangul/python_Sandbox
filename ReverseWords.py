class ReverseWords:

    def reverse(self, sentence):
        _words = sentence.split()
        return ' '.join(self.reverse_list(_words))

    def reverse_list(self, _list):
        if len(_list) == 0:
            return "nothing to reverse"
        if len(_list) == 1:
            return _list
        else:
            return [_list[-1]] + self.reverse_list(_list[:-1])


if __name__ == "__main__":
    print("Output: {}".format(ReverseWords().reverse(" Lili petite ma")))
