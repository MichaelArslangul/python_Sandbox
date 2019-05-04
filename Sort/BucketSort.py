import math
from collections import defaultdict

class BucketSort:

    def __init__(self, arr):
        self.arr = arr
        self.arr_l = len(arr)
        self.arr_max = max(arr)
        self.number_of_buckets = 10
        self.divider = 0
        self.buckets = defaultdict(list)

    def find_divider(self):
        self.divider = math.ceil((self.arr_max +1) / self.number_of_buckets)
        return self.find_divider

    def arrange_in_buckets(self):
        for _value in self.arr:
            _temp = _value // self.divider
            self.add_to_buckets_in_order(_temp, _value)

    def add_to_buckets_in_order(self, index, value):
        if not self.buckets[index]:
            self.buckets[index].append(value)
        else:
            for i in range(len(self.buckets[index])):
                if value < self.buckets[index][i]:
                    self.buckets[index].insert(i, value)
            if value not in self.buckets[index]:
                self.buckets[index].append(value)

    def bucket_sort(self):
        self.find_divider()
        self.arrange_in_buckets()
        _sorted_keys = sorted(self.buckets.keys())
        for i in _sorted_keys:
            if len(self.buckets[i]) > 1:
                for j in self.buckets[i]:
                    print(j)
            else:
                print(self.buckets[i][0])


a = [22, 45, 12, 8, 10 ,6, 72, 81, 33, 18,50,14]
bucket = BucketSort(a)
bucket.bucket_sort()
