# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

'''
test case:
1. empty list
2. there is only one node in the list
3. more than one node
'''

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # check if it's empty list
        if head==None:
            # empty list
            return None
        elif head.next == None:
            # only one node in the list, return itself.
            return head
        else:
            # more than one node
            idx1 = None # the former node
            idx2 = head # the node
            idx3 = head.next # the latter node
            while idx2.next!=None:
                idx2.next = idx1
                idx1 = idx2
                idx2 = idx3
                idx3 = idx3.next
            idx2.next = idx1
            return idx2


