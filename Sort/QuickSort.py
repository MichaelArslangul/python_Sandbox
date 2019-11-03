import random

def quicksort(items):
    """
    quickSort using a random pivot.
    """
    def sort(lst, l, r):
        # base case
        if r <= l:
            return

        # choose random pivot
        pivot_index = random.randint(l, r)

        # move pivot to first index
        lst[l], lst[pivot_index] = lst[pivot_index], lst[l]

        # partition
        i = l
        for j in range(l+1, r+1):
            if lst[j] < lst[l]:
                i += 1
                lst[i], lst[j] = lst[j], lst[i]

        # place pivot in proper position
        lst[i], lst[l] = lst[l], lst[i]

        # sort left and right partitions
        sort(lst, l, i-1)
        sort(lst, i+1, r)

    if items is None or len(items) < 2:
        return

    sort(items, 0, len(items) - 1)

alist = [54,26,93,17,77,31,44,55,20]
quicksort(alist)
print(alist)
