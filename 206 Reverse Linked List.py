# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head==None:
            return None
        
        t=head
        l=0
        while t!=None:
            l+=1
            t=t.next
        if l==1:
            return head
        if l==2:
            p1=head
            p2=head.next
            
            p1.next=None
            p2.next=p1
            
            return p2
        
        p1=head
        p2=p1.next
        p3=p2.next
        
        p1.next=None
        
        
        while p3 != None:
            p2.next=p1
            p1=p2
            p2=p3
            p3=p3.next
        p2.next=p1    
            
            
        return p2
            
