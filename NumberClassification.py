from collections import defaultdict


class NumberClassification:

    def classify_range_of_numbers(self, number, show=None):
        _classification = defaultdict(int)
        for n in range(1, number):
            _classification[self.classify_numbers(n)] += 1
            if show is not None:
                print("number: {} is {}".format(
                    n, self.classify_numbers(n)))
        return _classification

    def classify_numbers(self, number):
        if self.sum_divisors(number) < number:
            return "deficient"
        elif self.sum_divisors(number) == number:
            return "perfect"
        elif self.sum_divisors(number) > number:
            return "abundant"

    def sum_divisors(self, number):
        _sum = 0
        for _d in self.find_divisors(number):
            _sum += _d
        return _sum

    def find_divisors(self, number):
        _divisors = []
        for n in range(1, number):
            if number % n == 0:
                _divisors.append(n)
        return _divisors


if __name__ == "__main__":
    print("the number 12 is {}".format(
        NumberClassification().classify_numbers(12)))
    print("Classify numbers between 1 and 7: {}".format(
        NumberClassification().classify_range_of_numbers(20000)))
