'''
面试题06. 从尾到头打印链表
输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。

示例 1：
输入：head = [1,3,2]
输出：[2,3,1]
 
限制：
0 <= 链表长度 <= 10000
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# test cases:
# head->None: return []
# head.next==None: return [head.val]
# [1,2,3,4,5]: [5,4,3,2,1]

# recursive solution
# 执行用时 :132 ms, 在所有 Python3 提交中击败了14.45%的用户
# 内存消耗 :23 MB, 在所有 Python3 提交中击败了100.00%的用户
class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        if head==None:
            return []
        else:
            return self.reversePrint(head.next)+[head.val]
'''
# reverse the List, then print it. time:O(N),space:O(1), but altered the list
# 执行用时 :76 ms, 在所有 Python3 提交中击败了23.56%的用户
# 内存消耗 :15.2 MB, 在所有 Python3 提交中击败了100.00%的用户
class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        if head==None:
            return []
        if head.next==None:
            return [head.val]
        
        tempf = head
        tempb = head.next
        tempf.next = None
        while tempb!=None:
            #print(tempf.val,tempb.val)
            temp = tempb.next
            tempb.next = tempf
            tempf = tempb
            tempb = temp
            if temp!=None:
                temp = temp.next
        ans = []
        head = tempf
        while tempf!=None:
            ans.append(tempf.val)
            tempf = tempf.next
        return ans            
'''

'''
# print the List, save it in a list, then reverse it.time:O(N),space:O(N)
# 执行用时 :48 ms, 在所有 Python3 提交中击败了70.09%的用户
# 内存消耗 :15.1 MB, 在所有 Python3 提交中击败了100.00%的用户

class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        if head==None:
            return []
        if head.next==None:
            return [head.val]
        
        temp = head
        ans = []
        while temp!=None:
            ans.append(temp.val)
            temp=temp.next
        ans.reverse()
        return ans
'''
