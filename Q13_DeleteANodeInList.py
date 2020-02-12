# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#test cases:
#1. the node needed to be deleted is in the middle
#2. the node is at the end of the list
#3. only have one node in the list, and we want to delete it

class Solution(object):
    def deleteNode(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        tempNode=ListNode(0)
        tempNode.next=head
        if head.val==val: return head.next
        while head!=None and head.next!=None:
            if head.next.val==val:
                head.next=head.next.next
            head = head.next
        return tempNode.next
        
