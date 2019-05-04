import math
import collections
""" Leetcode number 996
"""

class NumberOfSquarefulArrays:

    def nbr_of_squareful_arrays(self, A):
        counter = collections.Counter(A)
        pairs = {x: {y for y in counter if int((x + y)**0.5) == (x + y)**0.5} \
                 for x in counter}


    # def nbr_of_squareful_arrays(self, A):
    #     self.mem = set()
    #     if len(A) <= 1:
    #         return 0
    #     _result = 0
    #     for i in range(len(A)):
    #         if A[i] == A[i-1]: continue
    #         _result += self.nbr_of_square_arrays([A[i]], A[:i] + A[i+1:])
    #     return _result
    #
    # def nbr_of_square_arrays(self, value, array):
    #     _temp = []
    #     _ans = 0
    #     if tuple(value) not in self.mem and len(array) == 0:
    #         self.mem.add(tuple(value))
    #         return 1
    #
    #     for j in range(len(array)):
    #         if self.is_square(array[j] + value[-1]):
    #             _temp.append(array[j])
    #             _ans += self.nbr_of_square_arrays(_temp, array[:j] + array[j+1:])
    #     return _ans
    #
    # def is_square(self, number):
    #     return int(math.sqrt(number)) - math.sqrt(number) == 0



#         def findPerm(A):
#             if A in mem: return mem[A]
#             if len(A) == 1: return set([A]) #base case
#             res = set()
#             for i in range(len(A)):
#                 prefixes = findPerm(A[:i] + A[i + 1:])
#                 for prefix in prefixes:
#                     if (prefix[-1] + A[i])**0.5 == int((prefix[-1] + A[i])**0.5):
#                         res.add(prefix + (A[i],))
#             mem[A] = res
#             return res
#         A, mem = tuple(sorted(A)), {}
#         return len(findPerm(A))

sa = NumberOfSquarefulArrays()
A = [2,2,2]
# A = [1,17,8]
# A = [2,2,2,2,2,2,2,2,2,2,2]
# A=[18,10,5,3]
# A=[1,6,1]
# A = [2,4,5,7,10,14]
# A = [18,0,16,2]
# A= [1,2,3,4,5,6,7,8] #36/8
print("number of squareful arrays: {}".format(
    sa.nbr_of_squareful_arrays(A)))


def nbr_of_squareful_arrays(self, values, A):
    self.mem = set()
    if len(A) <= 1:
        return 0
    _result = 0
    for i in range(len(A)):
        print("i: {}, A[i]: {}, A[:i] + A[i+1:]: {}".format(i, A[i], A[:i] + A[i+1:]))
        _result += self.nbr_of_square_arrays([A[i]], A[:i] + A[i+1:])
    return _result

def nbr_of_square_arrays(self, value, array):
    _temp = []
    _ans = 0
#     # if tuple(value) not in self.mem and len(array) == 0:
#     #     self.mem.add(tuple(value))
#     #     print(self.mem)
#     #     print("in return 1 value: {} and array: {}".format(value, array))
#     #     print()
#     #     return 1
    if tuple(value) not in self.mem and len(array) == 0:
        self.mem.add(tuple(value))
        print(self.mem)
        print("in return 1 value: {} and array: {}".format(value, array))
        print()
        return 1

    for j in range(len(array)):
        _temp = value
        if self.is_square(array[j] + value[-1]):
            print("value: {}, array: {}".format(value, array))
            # value.append(array[j])
            _temp.append(array[j])
            _ans += self.nbr_of_square_arrays(_temp, array[:j] + array[j+1:])
    return _ans
