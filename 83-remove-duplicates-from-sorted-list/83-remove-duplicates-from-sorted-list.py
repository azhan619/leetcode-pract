# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if(head == None or head.next == None):
            return head
        first = head
        second = head.next
        
        while(second):
            
            if(first.val == second.val):
                if(second.next):
                    first.next = second.next
                    second = second.next
                else:
                    first.next = None
                    second = None
            else:
                first = first.next
                second = second.next
        return head