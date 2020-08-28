'''
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

示例:
给定 1->2->3->4, 你应该返回 2->1->4->3.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/swap-nodes-in-pairs
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 执行用时：40 ms, 在所有 Python3 提交中击败了75.43%的用户
# 内存消耗：13.8 MB, 在所有 Python3 提交中击败了18.73%的用户
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head==None or head.next==None:
            return head
        
        t1 = head
        t2 = head.next
        newHead = t2
        pre = None

        while t1!=None and t2!=None:
            temp = t2.next
            t2.next = t1
            t1.next = temp
            if pre!=None:
                pre.next = t2
            #---shift
            pre = t2.next
            t1 = pre.next
            if t1==None:
                #print("break")
                t2==None
                break
            t2 = t1.next
        if t2==None:
            if t1==None:
                pre.next = None
            else:
                pre.next = t1
        return newHead
