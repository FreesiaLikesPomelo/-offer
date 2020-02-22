# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
'''
test case:	
1. 1->2->3,  4->5->6:  1->2->3->4->5->6
2. 1->2->4,  1->3->4:  1->1->2->3->4->4
3. both of the lists are empty lists
4. one of the lists is empty list
5. 
'''

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1==None:
            if l2==None:
                # both of the lists are empty lists
                return None
            else: # l1-empty, l2-normal
                return l2
        else:
            if l2==None:
                # l2-empty, l1-normal
                return l1
            else: # both are not empty lists
                idx_head = None

                if l1.val<=l2.val:
                    idx_head = l1
                    idx_head.next = self.mergeTwoLists(l1.next,l2)
                else:
                    idx_head = l2
                    idx_head.next = self.mergeTwoLists(l2.next,l1)
                return idx_head
                


    
