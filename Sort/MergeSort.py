class MergeSort:
    '''
    Practice merge sort
    '''

    def merge_sort(self, list):
        if len(list) ==1:
            return list
        else:
            i = 0
            j = 0
            k = 0
            middle = len(list)//2
            left = list[:middle]
            right = list[middle:]
            self.merge_sort(left)
            self.merge_sort(right)
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    list[k] = left[i]
                    i +=1
                else:
                    list[k] = right[j]
                    j +=1
                k += 1

            while i < len(left):
                if left[i] is not None:
                    list[k] = left[i]
                k +=1
                i +=1

            while j < len(right):
                if right[j] is not None:
                    list[k] = right[j]
                k +=1
                j +=1

        return list



l = [5,3,7,2,8,1,9,4,12,10,18,299,100,11,198,13,17,71,0]
ms = MergeSort()
print(ms.merge_sort(l))
