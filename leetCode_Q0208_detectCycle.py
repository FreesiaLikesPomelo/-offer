'''
面试题 02.08. 环路检测
难度 中等

给定一个链表，如果它是有环链表，实现一个算法返回环路的开头节点。
有环链表的定义：在链表中某个节点的next元素指向在它前面出现过的节点，则表明该链表存在环路。
 
示例 1：
输入：head = [3,2,0,-4], pos = 1
输出：tail connects to node index 1
解释：链表中有一个环，其尾部连接到第二个节点。
 
示例 2：
输入：head = [1,2], pos = 0
输出：tail connects to node index 0
解释：链表中有一个环，其尾部连接到第一个节点。
 
示例 3：
输入：head = [1], pos = -1
输出：no cycle
解释：链表中没有环。
 
进阶：
你是否可以不用额外空间解决此题？
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# hashtable -> SC:O(N)

# fast/slow pointers can denote if there's a ring in it
# 执行用时：68 ms, 在所有 Python3 提交中击败了45.18%的用户
# 内存消耗：16.7 MB, 在所有 Python3 提交中击败了59.17%的用户
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head==None or head.next==None:
            return 
        if head.next==head:
            return head
        if head.next.next==None:
            return None # [1,2] pos:0/1 there is a ring
        
        fast = head.next.next
        slow = head.next
        flag = 0
        while fast!=None and fast.next!=None:
            if fast==slow:
                # there is a ring in it
                flag = 1
                break
            else:
                slow = slow.next
                fast = fast.next.next
        if flag==0:
            return 
        fast = head
        while fast!=None and fast.next!=None:
            if fast==slow:  
                return fast
            else:
                fast = fast.next
                slow = slow.next
