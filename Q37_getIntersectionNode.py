'''
面试题52. 两个链表的第一个公共节点
输入两个链表，找出它们的第一个公共节点。

执行用时 :168 ms, 在所有 Python3 提交中击败了88.35%的用户
内存消耗 :28.5 MB, 在所有 Python3 提交中击败了100.00%的用户
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# test cases:
# 1. empty head: return None
# 2. two seperated list: return None
# 3. function test

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA==None or headB==None:
            return None
        
        # calculate the length of each list
        A = headA
        lenA = 0
        while A!=None:
            lenA+=1 
            #print("listA:",A.val)
            A = A.next
        
        B = headB
        lenB = 0
        while B!=None:
            lenB+=1
            #print("listB:",B.val)
            B = B.next
        #print(lenA,lenB)

        # travel longer list first:
        if lenA>lenB:
            dist = lenA - lenB
            shoLen = lenB
            lon = headA
            short = headB
        elif lenB>lenA:
            dist = lenB - lenA
            shoLen = lenA
            lon = headB
            short = headA
        else:
            dist = 0
            shoLen = lenA
            lon = headA
            short = headB

        if dist>0:
            for i in range(dist):
                #print("travel the longer one first:", lon.val)
                lon = lon.next

        for i in range(shoLen):
            #print(lon.val)
            #if lon.next==short.next:
            #    print("lon.next:",lon.next,"short.next:",short.next)
            #if lon.val==short.val and lon.next==short.next:
            if lon==short:
                result = lon.val
                #print("Found it!",result)
                return lon
            lon = lon.next
            short = short.next
        
        return None

'''
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA==None or headB==None:
            return None

        # travel two list, and save them in stack
        A = headA
        B = headB
        Astack = []
        Bstack = []
        while A!=None:
            Astack.append(A)
            A = A.next
        while B:
            Bstack.append(B)
            B = B.next
        #print("listA",Astack,"listB",Bstack)

        # find the first common node
        tempA = Astack.pop()
        tempB = Bstack.pop()
        if tempA==tempB:
            result = tempA
        else:
            return None

        while Astack!=[] and Bstack!=[]:
            tempA = Astack.pop()
            tempB = Bstack.pop()
            if tempA==tempB:
                result = tempA
            else:
                #print("Found it!",result)
                return result
        return result
'''


        
