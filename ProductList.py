class ProductList:
    """ Given an array nums of n integers where n > 1,
    return an array output such that output[i] is equal to
    the product of all the elements of nums except nums[i].
    Solve without division and in O(n).
    """

    def productExceptSelf(self, nums):
        rtype = []
        prod = 1
        for e in range(len(nums)):
            if e == 0:
                rtype.append(prod)
            else:
                prod *= nums[e-1]
                rtype.append(prod)

        back_prod = 1
        for e in range(len(nums)-1, -1, -1):
            if e == len(nums)-1:
                rtype[e] *= back_prod
            elif e < len(nums)-1:
                back_prod *= nums[e+1]
                rtype[e] *= back_prod
        return rtype





prod = ProductList()
print("result: {}".format(prod.productExceptSelf([2,3,4,5])))
