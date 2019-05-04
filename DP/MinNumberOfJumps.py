class MinNumberOfJumps:
    """ Given  an array, what's the minimum number of jumps we can take to
    reach the end
    """


    def min_jumps(self, array):
        N = len(array)
        _res = {}
        _ans=[]
        _temp = float('inf')
        _ans.append(N-1)
        while _ans:
            i = _ans.pop()
            if i > 0:
                for j in range(1, i+1):
                    # print("i: {}, j: {}, array[i - j]: {}".format(i,j, array[i - j]))
                    if array[i - j] >= j: # i = 9, j =1; i = 1, j = 1
                        _temp = min(_temp, i - j)
                _res[i] = _temp
                _ans.append(_temp)
            else:
                break
        print(_res)
        return len(_res)

        # for i in range(N-1, 1, -1):
        #     for j in range(1, i+1):
        #         print("i: {}, j: {}, array[i - j]: {}".format(i,j, array[i - j]))
        #         if array[i - j] >= j: # i = 9, j =1; i = 1, j = 1
        #             _temp = min(_temp, i - j)
        #     _res[i] = _temp
        # print(_res)
        # s = set(_res.values())
        # return len(s)


mn = MinNumberOfJumps()
array = [1,7,3,4,6,155, 23]
# array = [2,3,1,1,2,4,2,0,1,1]
print("Number of jumps: {} for array: {}".format(
    mn.min_jumps(array), array))
