class Sum:

    def calculate_sum(self, numbers):
        if len(numbers) == 0:
            return 0

        return numbers[0] + self.calculate_sum(numbers[1:])


sum = Sum()
print("sum: {}".format(sum.calculate_sum([1, 2, 3, 4, 5, 6])))
