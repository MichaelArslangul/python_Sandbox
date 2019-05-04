class AddSortedLists:

    def add_lists1(self, first, second):
        return sorted(first + second)

    def add_lists2(self, first, second):
        result = []
        while first and second:
            if first[0] < second[0]:
                result.append(first[0])
                first.pop(0)
            else:
                result.append(second[0])
                second.pop(0)
        if len(first) > 0:
            return result + first
        if len(second) > 0:
            return result + second
        return result


add_l = AddSortedLists()
first = [0, 2, 4, 6, 8, 10, 12]
second = [1, 3, 5, 7, 9]
print("new lists created from first: {} and second: {} is: {}".format(
    first, second, add_l.add_lists2(first, second)
))
