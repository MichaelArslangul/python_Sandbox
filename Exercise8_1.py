class Exercise8_1:

    def count_ways(self, n):
        if n == 0:
            return 1
        else:
            return self.count_ways(n - 1) + \
                self.count_ways(n - 2) + \
                self.count_ways(n - 3)


exo = Exercise8_1()
print("How many ways to get up 4 stairs: {}".format(exo.count_ways(4)))
