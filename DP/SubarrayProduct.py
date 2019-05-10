class SubarrayProduct:
    """ Leetcode 713
    """

    def numSubarrayProductLessThanK(self, nums, k) -> int:
        _res = [[0] * (len(nums) + 1)]
        if len(nums) == 0:
            return 0
        elif len(nums) == 1 and input[-1] < k:
            return 1
        # if nums[0] < k:
        #     _res[0] = [nums[0]]
        for i in range(1, len(nums)+1):
            if nums[i] < k:
                # 2 possibilities, nums[i] is part of the product or it isn't
                _res.append([k])
                for j in range(i):
                    if _res[i-1] * nums[i] <k:
                        _res[i] = _res[i - 1].append(nums[i])
                    elif _res[i-1][j:] < k:
                        _res[i] = _res[i - 1][j:]
        print(_res)
        




sp = SubarrayProduct()
nums = [10, 5, 2, 6]
k = 100
print("subarrays where the product is less than {} are/is: {}".format(
    k, sp.numSubarrayProductLessThanK(nums, k)))
