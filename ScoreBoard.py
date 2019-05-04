class ScoreBoard:

    def __init__(self, capacity = 10):
        self.capacity = capacity
        self._scoreboard = []

    def __getitem__(self, key):
        return _scoreboard[key]

    def __str__(self):
        _ans = []
        for i in self._scoreboard:
            _ans.append(str(i))
        return ' | '.join(_ans)


    def add(self, entry):
        score = entry.get_score()
        if len(self._scoreboard) == 0:
            self._scoreboard.append(entry)

        great_score = len(self._scoreboard) < self.capacity or \
            score > self._scoreboard[0].get_score()

        if great_score:
            print(entry)
            if len(self._scoreboard) == self.capacity:
                self._scoreboard.pop(0)
            self.in_order_sort(entry)

    def in_order_sort(self, entry):
        nbr_scores = len(self._scoreboard) - 1
        for j in range(nbr_scores, -1, -1):
            if entry.get_score() > self._scoreboard[j].get_score():
                self._scoreboard.insert(j+1, entry)
                break
        if entry not in self._scoreboard:
            self._scoreboard.insert(0, entry)
        return self._scoreboard



class GameEntry:

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_name(self):
        return self.name

    def get_score(self):
        return self.score

    def __str__(self):
        return "({}, {})".format(self.name, self.score)

sc = ScoreBoard(4)
mi_entry = GameEntry("michael", 1)
gab_entry = GameEntry("Gabrielle", 20)
lili_entry = GameEntry("Lili", 3)
annie_entry = GameEntry("annie", 4)
arnaud_entry = GameEntry("arnaud", 5)
angeline_entry = GameEntry("angeline", 6)
elodie_entry = GameEntry("elodie", 7)
sc.add(gab_entry)
sc.add(lili_entry)
sc.add(arnaud_entry)
sc.add(elodie_entry)
sc.add(angeline_entry)
sc.add(annie_entry)
print("outcome: {}".format(sc))
