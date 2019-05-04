class FindMissing:

    def find_missing(self, array_orig, array_missing):
        set_orig = set(array_orig)
        set_missing = set(array_missing)
        return set_orig - set_missing

    def find_missing_xor(self,array_orig, array_missing):
        xor_num = 0
        for i in array_orig:
            xor_num ^= i
        for j in array_missing:
            xor_num ^= j
        return xor_num

fm = FindMissing()
array=[4,12,9,5,6]
array_2=[4,9,12,5]

print("missing element between array: {} and array: {} is: {}".format(
    array, array_2, fm.find_missing(array, array_2)
))
print("missing element between array: {} and array: {} is: {}".format(
    array, array_2, fm.find_missing_xor(array, array_2)
))
