import math

class ShortestSubsrrayRPositif:
    """
    Return the length of the shortest, non-empty, contiguous subarray of s
    with sum at least blah.
    IN this version, numbers will positif

    If there is no non-empty subarray with sum at least blah, return -1
    """
    def shortest_subarray(self, s, nums):
        N=len(nums)
        _sum =0
        left =0
        _result =math.inf
        if len(nums) == 0:
            return 0
        elif max(nums) >=s:
            return 1
        else:
            for i in range(N):
                _sum += nums[i]
                while _sum >=s:
                    _result = min(_result, i + 1-left) #i +1
                    _sum -= nums[left]
                    left +=1

        return _result if not _result == math.inf else 0

sa = ShortestSubsrrayRPositif()
print(sa.shortest_subarray(80,[10,5,13,4,8,4,5,11,14,9,16,10,20,8]))
print(sa.shortest_subarray(15, [5,1,3,5,10,7,4,9,2,8]))
print(sa.shortest_subarray(3,[])) # result is 2
print(sa.shortest_subarray(3,[2,2])) # result is 2
print(sa.shortest_subarray(4,[1,2])) # 0
print(sa.shortest_subarray(4, [1,2,3])) # 2
print(sa.shortest_subarray(20, [1,2,3,4])) # 0
print(sa.shortest_subarray(1, [1])) # 1
print(sa.shortest_subarray(10, [1,2,3,4,5,6,7,8,9])) #2
print(sa.shortest_subarray(150, [1,98,56,1,10])) # 2
