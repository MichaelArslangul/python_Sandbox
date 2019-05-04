class Sparselist:
    """
    Given a list of strings with spaces, find the index
    of a particular word:
    {"je", "", "", "suis"}
    "suis" est a index: 3
    """

    def __init__(self, slist):
        self.slist = slist

    def index_of(self, word):
        if word not in self.slist:
            raise ValueError("word " + word + " is not in list")
        else:
            _dict = dict(enumerate(self.slist))
            for key, value in _dict.items():
                if value == word:
                    return key


slist = ["tout", "", "", "corps", "", "plonge", "dans", "", "",
         "", "fluide", "", "recoit"]
slist = Sparselist(slist)
print("index of word: plonge is: {}".format(
    slist.index_of("tocard")))
