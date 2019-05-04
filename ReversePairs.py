import bisect

class ReversePairs:
    """
    Given an array nums, we call (i, j) an important reverse pair if i < j
    and nums[i] > 2*nums[j].

    You need to return the number of important reverse pairs
    in the given array.

    Example1:
    Input: [1,3,2,3,1]
    Output: 2

    Example2:
    Input: [2,4,3,5,1]
    Output: 3
    """
    # def __init__(self):
    #     self.count = 0

    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        lst = []
        while nums:
            num = nums.pop()
            index = bisect.bisect_left(lst, float(num)/2)
            result += index
            bisect.insort(lst, num)
        # print(lst)
        return result




rp = ReversePairs()
print(rp.reversePairs([5,4,3,2,1]))


    #     self.mergesort(nums)
    #     return self.count
    #
    # def mergesort(self, lst):
    #     if len(lst)<=1:
    #         return lst
    #
    #
    #     _middle  = len(lst)//2
    #     left = lst[:_middle]
    #     right = lst[_middle:]
    #     self.mergesort(left)
    #     self.mergesort(right)
    #     i = 0
    #     j = 0
    #
    #     while i < len(left) and j < len(right):
    #         if left[i] > 2*right[j]:
    #             self.count += len(left) - i
    #             j += 1
    #         else:
    #             if i +1 == len(left) and j < len(right):
    #                 j +=1
    #             else:
    #                 i +=1
    #     return sorted(left+right)
