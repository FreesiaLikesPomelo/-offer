# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#　stack: 逆序处理
# 执行用时：96 ms, 在所有 Python3 提交中击败了34.87%的用户
# 内存消耗：13.7 MB, 在所有 Python3 提交中击败了67.86%的用户
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1==None:
            return l2
        if l2==None:
            return l1

        stack1 = []
        temp = l1
        while temp!=None:
            stack1.append(temp.val)
            temp = temp.next
        stack2 = []
        temp = l2
        while temp!=None:
            stack2.append(temp.val)
            temp = temp.next
        
        carry = 0
        dummy = ListNode(-1)
        while stack1!=[] and stack2!=[]:
            s = stack1.pop()+stack2.pop()+carry
            if s>=10:
                s = s%10
                ans = s
                carry = 1
            else:
                ans = s
                carry = 0
            new = ListNode(ans)
            if dummy.next==None:
                dummy.next = new
            else:
                t = dummy.next
                dummy.next = new
                new.next = t
        if stack1==[]:
            while stack2!=[]:
                ans = stack2.pop()+carry
                if ans>=10:
                    ans = ans%10
                    carry = 1
                else:
                    carry = 0
                new = ListNode(ans)
                if dummy.next==None:
                    dummy.next = new
                else:
                    t = dummy.next
                    dummy.next = new
                    new.next = t
        if stack2==[]:
            while stack1!=[]:
                ans = stack1.pop()+carry
                if ans>=10:
                    ans = ans%10
                    carry = 1
                else:
                    carry = 0
                new = ListNode(ans)
                if dummy.next==None:
                    dummy.next = new
                else:
                    t = dummy.next
                    dummy.next = new
                    new.next = t
        if carry!=0:
            new = ListNode(1)
            carry = 0
            if dummy.next==None:
                dummy.next = new
            else:
                t = dummy.next
                dummy.next = new
                new.next = t
        return dummy.next
        

'''
# 执行用时：108 ms, 在所有 Python3 提交中击败了12.89%的用户
# 内存消耗：13.8 MB, 在所有 Python3 提交中击败了28.90%的用户
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1==None:
            return l2
        if l2==None:
            return l1
        
        temp = l1
        num1 = temp.val
        while temp.next!=None:
            num1 = num1*10+temp.next.val
            temp = temp.next
        # print("the value of l1 is:",num1)

        temp = l2
        num2 = temp.val
        while temp.next!=None:
            num2 = num2*10+temp.next.val
            temp = temp.next
        # print("the value of l2 is:",num2)

        s = num1+num2
        # print("the value of the sum of l1 and l2 is:",s)
        if s==0:
            ans = ListNode(0)
            return ans

        dummy = ListNode(-1) # dummy Node
        # quotient; remainder

        while s/10>0:
            remainder = s%10
            quotient = s//10
            # print(s,remainder,quotient)
            s = quotient
            temp = ListNode(remainder)
            if dummy.next==None:
                dummy.next = temp
            else:
                tt = dummy.next
                dummy.next = temp
                temp.next = tt
        return dummy.next
'''
