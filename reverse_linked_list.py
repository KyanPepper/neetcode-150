class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        
        stack = []
        while head is not None:
            stack.append(head)
            head = head.next
        
        ret = stack[-1]
        while len(stack) > 0:
            node :ListNode = stack.pop()
            if(stack):
                node.next=stack[-1]
            else:
                node.next = None
        return ret
        