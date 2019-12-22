class LargestRange:

    def largestRange(self, array):
        no_dups = list(set(array))
        sorted_array = sorted(no_dups)
        longest_range = [[sorted_array[0], sorted_array[0]]]
        for i in range(1, len(sorted_array)):
            if sorted_array[i] == sorted_array[i-1] + 1:
                longest_range[0][-1] = sorted_array[i]
            else:
                longest_range.insert(0, [sorted_array[i], sorted_array[i]])
        return self.range_size(longest_range)

    def range_size(self, array):
        dict_ranges = {}
        for range in array:
            dict_ranges[abs(range[-1] - range[0])] = range
        return dict_ranges[max(dict_ranges.keys())]

lr = LargestRange()
print("largest range: {}".\
      format(lr.largestRange([-7,-7,-7,-7,8,-8,0,9,19,-1,-3,18,17,2,10,3,12,5,16,4,11,-6,8,7,6,15,12,12,-5,2,1,6,13,14,-4,-2])))
[-7,-7,-7,-7,8,-8,0,9,19,-1,-3,18,17,2,10,3,12,5,16,4,11,-6,8,7,6,15,12,12,-5,2,1,6,13,14,-4,-2]
# [1,11,3,0,15,5,2,4,10,7,12,6]
