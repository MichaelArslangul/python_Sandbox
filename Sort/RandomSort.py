import random


class RandomSort:
    '''
    random.random()
    '''

    def r_sort(self, list):
        n = len(list)
        for i in range(n-1, -1, -1):
            _rand = random.randint(0, i)
            _temp = list[i]
            list[i] = list[_rand]
            list[_rand] = _temp
        return list


if __name__ == "__main__":
    print("Random sort of [1, 0, 3, 9, 2] is: {}".format(
        RandomSort().r_sort([1, 0, 3, 9, 2])))
