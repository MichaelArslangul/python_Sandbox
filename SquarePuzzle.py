from itertools import permutations


class SquarePuzzle:

    def equality(self, a, b, c, d, e, f, g):
        return a+b == b+c+d == d+e+f == f+g

    def find_permutations(self, low_high):
        return permutations(low_high)


    def solve_puzzle(self, LOW, HIGH, unique=None, show=None):
        _list = self.find_permutations(list(range(LOW, HIGH+1)))
        _solutions = 0
        for i in _list:
            if self.equality(*i):
                _solutions += 1
                if show == "show":
                    print("Those values meet our criteria: {}".format(i))
        print("There are {} solutions to the problem, \
with LOW = {} and HIGH = {}".format(_solutions, LOW, HIGH))


sqr_p = SquarePuzzle()
sqr_p.solve_puzzle(1, 7, 'unique', 'show')
sqr_p.solve_puzzle(3, 9, 'unique')
