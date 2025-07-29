from typing import Optional
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        prev = dummy
        curr = head

        while curr and curr.next:
            next_pair = curr.next.next
            tmp = curr.next
            tmp.next = curr
            curr.next = next_pair
            prev.next = tmp
            prev = curr
            curr = next_pair

        return dummy.next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        prev = dummy
        curr = head

        while curr and curr.next:
            next_pair = curr.next.next
            tmp = curr.next
            tmp.next = curr
            curr.next = next_pair
            prev.next = tmp
            prev = curr
            curr = next_pair

        return dummy.next

