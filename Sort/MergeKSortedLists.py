from bisect import insort_left

class MergeKSortedLists:

    """
    Merge k sorted linked lists and return it as one sorted list.

    Example:

    Input:
    [
      1->4->5,
      1->3->4,
      2->6
    ]
    Output: 1->1->2->3->4->4->5->6
    """

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class MergeKSortedLists:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        _result = []
        for i in lists:
            while i is not None:
                insort_left(_result, int(i.val))
                i =  i.next
        return _result



list_node1 = ListNode('1')
list_node1.next = ListNode('4')
list_node1.next.next = ListNode('5')
list_node2 = ListNode('1')
list_node2.next = ListNode('3')
list_node2.next.next = ListNode('4')
list_node3 = ListNode('2')
list_node3.next = ListNode('6')
mkl = MergeKSortedLists()
print(mkl.mergeKLists([list_node1, list_node2, list_node3]))
