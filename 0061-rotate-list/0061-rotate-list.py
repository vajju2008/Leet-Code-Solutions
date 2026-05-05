# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head, k):
        if not head or not head.next or k == 0: return head  

        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1  

        k %= length
        if k == 0: return head 

        tail.next = head  # circular

        steps = length - k
        newtail = head
        for _ in range(1, steps):
            newtail = newtail.next  

        newhead = newtail.next  
        newtail.next = None  

        return newhead