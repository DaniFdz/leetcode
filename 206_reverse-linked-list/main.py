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
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         s = []
#
#         while head != None:
#             s.append(head.val)
#             head = head.next
#
#         new_head = ListNode(0)
#         current = new_head
#         while s:
#             v = s.pop()
#             current.next = ListNode(v)
#             current = current.next
#
#         return new_head.next

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p = None
        c = head
        while c:
            n = c.next
            c.next = p
            p = c
            c = n

        return p

if __name__ == '__main__':
    s = Solution().reverseList
    assert s(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))).__str__() == ListNode(5, ListNode(4, ListNode(3, ListNode(2, ListNode(1))))).__str__()
    assert s(ListNode(1, ListNode(2))).__str__() == ListNode(2, ListNode(1)).__str__()
    assert s(ListNode()).__str__() == ListNode().__str__()
