class Derangement:

    def derangement_of_set(self, number):
        if number == 0:
            return 1
        if number == 1:
            return 0
        return (number - 1)*(self.derangement_of_set(number - 1)
                             + self.derangement_of_set(number - 2))


derang = Derangement()
for i in range(14):
    print("derangement {}: {}".format(i, derang.derangement_of_set(i)))
