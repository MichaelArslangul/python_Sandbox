class ReverseList:

    def reverse(self, list):
        s = len(list)
        if s == 0:
            return []
        if s == 1:
            return list
        elif s > 1:
            return [list[-1]] + self.reverse(list[:-1])


if __name__ == "__main__":
    print("Reverse list: [] is: {}".format(
        ReverseList().reverse([])))
    print("Reverse list: [1] is: {}".format(
        ReverseList().reverse([1])))
    print("Reverse list: [1,2,3] is: {}".format(
        ReverseList().reverse([1, 2, 3])))
    print("Reverse list: [1,7,5,2] is: {}".format(
        ReverseList().reverse([1, 7, 5, 2])))
