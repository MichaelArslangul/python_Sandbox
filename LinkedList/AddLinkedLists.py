class ListNode:

    def __init__(self, value):
        self.val = value
        self.next = None

    def __repr__(self):
        return "Node <{}>\n".format(self.val)

class AddLinkedLists:
    """ Leetcode2
    """
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 342 + 465
        root = _result = ListNode(0)
        _remainder = 0
        if l1.val == 0 and l2.val == 0:
            return ListNode(0)
        while l1 or l2 or _remainder:
            _val1 = _val2 = 0
            if l1:
                _val1 = l1.val
                l1 = l1.next
            if l2:
                _val2 = l2.val
                l2 = l2.next
            _result.next = ListNode((_val1 + _val2) %10 + _remainder)
            if _val1 + _val2 + _remainder >= 10:
                _remainder = 1
            else:
                _remainder =0
            _result = _result.next
        return root.next





first = ListNode(2)
first.next = ListNode(4)
first.next.next = ListNode(3)
second = ListNode(5)
second.next = ListNode(6)
second.next.next = ListNode(4)
fc = AddLinkedLists()
_temp = fc.addTwoNumbers(first, second)
while _temp:
    print(_temp)
    _temp = _temp.next
