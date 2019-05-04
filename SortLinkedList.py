class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class SortLinkedList:
    """
    Sort a linked list in O(n log n) time using constant
    space complexity.

    Example 1:

    Input: 4->2->1->3
    Output: 1->2->3->4

    Example 2:

    Input: -1->5->3->4->0
    Output: -1->0->3->4->5
    """
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        _temp = []
        _list = []
        ans = _node = ListNode(0)
        node = head
        while node is not None:
            _temp.append(node.val)
            node = node.next
        _list = sorted(_temp)
        for i in _list:
            _node.next = ListNode(i)
            _node = _node.next
        return ans.next


list_node1 = ListNode('4')
list_node1.next = ListNode('2')
list_node1.next.next = ListNode('1')
list_node1.next.next.next = ListNode('3')
sl = SortLinkedList()
node = sl.sortList(list_node1)
while node is not None:
    print(node.val)
    node = node.next
