from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        c = self
        s = ''
        while c != None:
            s += c.val.__str__() + ' '
            c = c.next

        return s.strip()

    def __repr__(self):
        return self.__str__()

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l = ListNode()
        c = l

        while list1 or list2:
            if list1 and list2:
                if list1.val < list2.val:
                    c.next = ListNode(list1.val)
                    list1 = list1.next
                else:
                    c.next = ListNode(list2.val)
                    list2 = list2.next

            elif list1:
                c.next = ListNode(list1.val)
                list1 = list1.next

            elif list2:
                c.next = ListNode(list2.val)
                list2 = list2.next

            c = c.next

        return l.next


if __name__ == '__main__':
    s = Solution().mergeTwoLists

    assert s(ListNode(1, ListNode(2, ListNode(4))), ListNode(1, ListNode(3, ListNode(4)))).__str__() == ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(4)))))).__str__()
    assert s(None, None).__str__() == None.__str__()
    assert s(None, ListNode(0)).__str__() == ListNode(0).__str__()
