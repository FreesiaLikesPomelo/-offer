'''
82. 删除排序链表中的重复元素 II
难度中等
给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 没有重复出现 的数字。
示例 1:
输入: 1->2->3->3->4->4->5
输出: 1->2->5
示例 2:
输入: 1->1->1->2->3
输出: 2->3
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 执行用时：40 ms, 在所有 Python3 提交中击败了98.64%的用户
# 内存消耗：13.6 MB, 在所有 Python3 提交中击败了74.19%的用户
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head==None or head.next==None:
            return head

        # #---test---#
        # temp = head
        # for i in range(0,5):
        #     temp = temp.next
        # temp.next.val = 4
        # print(head)
        
        # find the new head first
        pre = head 
        cur = head.next
        while pre.val==cur.val: # [1,1,1,2,2] [1,1,3,3,4,4,5]
            if cur.next==None:
                return None
            else:
                cur = cur.next
                while pre.val==cur.val:
                    if cur.next==None:
                        return None
                    cur = cur.next
                pre = cur
                if pre.next==None:
                    return pre
                else:
                    cur = pre.next
        newHead = pre
        prepre = pre
        pre = pre.next
        cur = pre.next
        while cur!=None:
            if pre.val!=cur.val:
                prepre = prepre.next
                pre = pre.next
                cur = cur.next
            else:
                if cur.next==None:
                    prepre.next = None
                    return newHead                
                cur = cur.next
                while pre.val==cur.val:
                    cur = cur.next
                    if cur==None:
                        prepre.next = None
                        return newHead
                prepre.next = cur
                pre = cur
                cur = cur.next
        return newHead
                
