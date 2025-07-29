from typing import Optional

class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy
        target = None
        curr = head
        i = 0
        while curr:
            if i == n:
                prev = prev.next
            else:
                i +=1
            curr = curr.next

        prev.next = prev.next.next
        return dummy.next