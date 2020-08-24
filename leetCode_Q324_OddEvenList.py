'''
328. 奇偶链表
难度 中等

给定一个单链表，把所有的奇数节点和偶数节点分别排在一起。请注意，这里的奇数节点和偶数节点指的是节点编号的奇偶性，而不是节点的值的奇偶性。
请尝试使用原地算法完成。你的算法的空间复杂度应为 O(1)，时间复杂度应为 O(nodes)，nodes 为节点总数。
示例 1:
输入: 1->2->3->4->5->NULL
输出: 1->3->5->2->4->NULL
示例 2:
输入: 2->1->3->5->6->4->7->NULL 
输出: 2->3->6->7->1->5->4->NULL
说明:
应当保持奇数节点和偶数节点的相对顺序。
链表的第一个节点视为奇数节点，第二个节点视为偶数节点，以此类推。
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
# recursive
# 执行用时：60 ms, 在所有 Python3 提交中击败了46.37%的用户
# 内存消耗：17.4 MB, 在所有 Python3 提交中击败了5.08%的用户
class Solution:
    def recurList(self,oddpre:ListNode, evenpre:ListNode, newhead:ListNode):
        # return None
        if newhead==None:
            return
        if newhead.next==None:
            self.oddpre.next = newhead
            self.oddpre = self.oddpre.next
            evenpre.next = None
            return
        if newhead.next.next==None:
            self.oddpre.next = newhead
            self.oddpre = self.oddpre.next
            evenpre.next = newhead.next
            evenpre = evenpre.next
            evenpre.next = None
            return
        
        self.oddpre.next = newhead
        self.oddpre = self.oddpre.next
        evenpre.next = newhead.next
        evenpre = evenpre.next
        newhead = newhead.next.next
        self.recurList(self.oddpre,evenpre,newhead)

    def oddEvenList(self, head: ListNode) -> ListNode:
        if head==None:
            return
        if head.next==None or head.next.next==None:
            return head

        oddhead = head
        evenhead = head.next
        newhead = evenhead.next
        evenpre = evenhead
        self.oddpre = oddhead

        self.recurList(self.oddpre, evenpre,newhead)
        self.oddpre.next = evenhead
        return oddhead
        

'''
# iteration
# 执行用时：52 ms, 在所有 Python3 提交中击败了86.15%的用户
# 内存消耗：15.6 MB, 在所有 Python3 提交中击败了80.96%的用户
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head==None:
            return
        if head.next==None or head.next.next==None:
            return head
        
        oddhead = head
        evenhead = head.next
        oddcur = head.next.next
        if oddcur.next==None:
            # only containing 3 nodes
            oddhead.next = oddcur
            oddcur.next = evenhead
            evenhead.next = None
            return oddhead
        else:
            evencur = oddcur.next
        oddpre = oddhead
        evenpre = evenhead
        while evencur!=None and evencur.next!=None:
            #print("~~oddcur:",oddcur.val," evencur:",evencur.val)
            oddpre.next = oddcur
            oddcur = oddcur.next.next
            oddpre = oddpre.next
            evenpre.next = evencur
            evencur = evencur.next.next
            evenpre = evenpre.next
            #print("@oddcur:",oddcur," evencur:",evencur)
        if evencur==None:
            oddpre.next = oddcur
            oddcur.next = evenhead
            evenpre.next = evencur
            return oddhead
            #print("oddcur:",oddcur," evencur:",evencur)
        else:
            #print("~oddcur:",oddcur.val," evencur:",evencur.val)
            # evencur.next==None
            oddpre.next = oddcur
            oddcur.next = evenhead
            evenpre.next = evencur
            evencur.next = None
            return oddhead
