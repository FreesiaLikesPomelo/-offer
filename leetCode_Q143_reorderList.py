'''
143. 重排链表难度中等287给定一个单链表 L：L0→L1→…→Ln-1→Ln ，
将其重新排列后变为： L0→Ln→L1→Ln-1→L2→Ln-2→…
你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
示例 1:
给定链表 1->2->3->4, 重新排列为 1->4->2->3.
示例 2:
给定链表 1->2->3->4->5, 重新排列为 1->5->2->4->3.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reorder-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#执行用时：112 ms, 在所有 Python3 提交中击败了66.84%的用户
#内存消耗：23.1 MB, 在所有 Python3 提交中击败了72.38%的用户
# find the middle node first
# then save the latters into a stack
# finally, insert the node popped from the stack
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head==None or head.next==None or head.next.next==None:
            return head
        
        fast = head
        slow = head
        while fast.next!=None and fast.next.next!=None:
            slow = slow.next
            fast = fast.next.next
        # slow is the middle node
        stack = []
        temp = slow.next
        while temp.next!=None:
            stack.append(temp)
            temp = temp.next
        stack.append(temp)
        temp.next = None # now temp is the last node of former half

        cur = head
        while stack!=[]:
            t = cur.next
            cur.next = stack.pop()
            cur.next.next = t
            cur = t
        if cur!=temp:
            cur.next = None
        return head


