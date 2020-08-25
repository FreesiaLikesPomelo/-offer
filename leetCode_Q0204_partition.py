'''
面试题 02.04. 分割链表
难度中等

编写程序以 x 为基准分割链表，使得所有小于 x 的节点排在大于或等于 x 的节点之前。如果链表中包含 x，x 只需出现在小于 x 的元素之后(如下所示)。分割元素 x 只需处于“右半部分”即可，其不需要被置于左右两部分之间。
示例:
输入: head = 3->5->8->5->10->2->1, x = 5
输出: 3->1->2->10->5->5->8
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 执行用时：44 ms, 在所有 Python3 提交中击败了70.76%的用户
# 内存消耗：13.8 MB, 在所有 Python3 提交中击败了26.07%的用户
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if head==None:
            return 
        if head.next==None:
            return head
        
        temp = head
        big = None
        small = None
        bigpre = big
        smallpre = small
        if head.val>=x:
            big = head
            bigpre = head 
            temp = temp.next
        else:
            small = head
            smallpre = head
            temp = temp.next
        while temp!=None:
            if temp.val>=x:
                if big==None: # big list is empty
                    big = temp
                    bigpre = big
                    temp = temp.next
                else:
                    bigpre.next = temp
                    bigpre = bigpre.next
                    temp = temp.next
            else:
                if small==None:
                    small = temp
                    smallpre = small
                    temp = temp.next
                else:
                    smallpre.next = temp
                    smallpre = smallpre.next
                    temp = temp.next
        if big==None:
            smallpre.next = None
            return small
        else:
            if small==None:
                bigpre.next = None
                return big
            else:
                smallpre.next = big
                bigpre.next = None
                return small
