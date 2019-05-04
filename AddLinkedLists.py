class AddLinkedLists:
    """
    Add 2 numbers represented by LinkedLists
    e.g:
    inputs:
    '5'=>'6'=>'3' and '8'=>'4'=>'2'
    output: '1'=>'4'='0'=>'5'
    """

    def add_l(self, link1, link2):
        result = 0
        list1 = 0
        list2 = 0
        for i in link1:



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
