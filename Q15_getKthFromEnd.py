# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

'''
test case:
1. lengthOfList>=k: function test
2. k <=0: meaning less
3. head.val==None: empty list
4. lengthOfList<k: return None
'''

class Solution(object):
    def getKthFromEnd(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
		# check if it's illegal input
        if head.val==None: 
            return None # head is Null, empty list.
        if k<=0: 
            return None # k<=0: meaning less
        else:
            idx1=head
            idx2=head
            for i in range(k-1):
                idx1=idx1.next
                if i<k-1-1 and idx1.next==None:
                    return None # the length of the list is smaller then k
            while idx1.next!=None:
                idx1=idx1.next
                idx2=idx2.next
            return idx2
				
			
