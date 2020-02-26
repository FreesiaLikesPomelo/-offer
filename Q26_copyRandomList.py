"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

"""
请实现 copyRandomList 函数，复制一个复杂链表。在复杂链表中，每个节点除了有一个 next 指针指向下一个节点，还有一个 random 指针指向链表中的任意节点或者 null。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/fu-za-lian-biao-de-fu-zhi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

执行用时 :48 ms, 在所有 Python3 提交中击败了54.03%的用户
内存消耗 :14 MB, 在所有 Python3 提交中击败了100.00%的用户
"""

# copy each node and add it just after the node
# build up the random for new node
# seperate it into two lists

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head==None:
            return None
        
        # copy each node and add it just after the node
        idx = head
        while idx.next!=None:
            temp = Node(idx.val, idx.next) # random = None
            idx.next = temp
            idx = idx.next.next
        temp = Node(idx.val)
        idx.next = temp 
        
        # build up the random for new node
        idx = head
        while idx!=None:
            if idx.random==None:
                if idx.next.next==None:
                    break
                else:
                    idx=idx.next.next
            else:
                idx.next.random = idx.random.next
                idx = idx.next.next

        # seperate it into two lists
        original = head
        newHead = head.next
        newTemp = head.next
        while newTemp.next!=None:
            original.next = original.next.next
            newTemp.next = newTemp.next.next
            original = original.next
            newTemp = newTemp.next
        original.next = None
        return newHead
