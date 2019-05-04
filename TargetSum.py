class TargetSum:
    """ Given  an integer  x and an unsorted  array of integers,  describe  an
    algorithm  to determine  whether two of  the numbers  add  up  to x.
    (In  this  case,  do not use Hashtables.)
    """


    def add_to_target_sum(self, array, target):
        _s_array = sorted(array)
        _front = _s_array[0]
        _end = _s_array[-1]
        i = j = 1
        while i < len(array) and j < len(array):
            if _front + _end == target:
                return True
            elif _front + _end > target:
                _end = _s_array[-1 -j]
                j += 1
            else:
                _front = _s_array[i]
                i += 1
        return False


ts = TargetSum()
array = [1,7,3,4,6,155, 23]
target = 161
print("Are there 2 elements of the array: {} that add up to: {}. The answer is: {}".format(
    array, target, ts.add_to_target_sum(array, target)))
