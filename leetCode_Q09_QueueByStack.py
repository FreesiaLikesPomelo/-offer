# 执行用时：572 ms, 在所有 Python3 提交中击败了62.12%的用户
# 内存消耗：16.9 MB, 在所有 Python3 提交中击败了100.00%的用户
class CQueue:
    def __init__(self):
        self.q = []

    def appendTail(self, value: int) -> None:
        self.q.append(value)

    def deleteHead(self) -> int:
        if self.q==[]:
            return -1
        else:
            return self.q.pop(0)           

'''
# 执行用时：572 ms, 在所有 Python3 提交中击败了62.12%的用户
# 内存消耗：16.9 MB, 在所有 Python3 提交中击败了100.00%的用户
class CQueue:
    def __init__(self):
        self.head = []
        self.tail = []

    def appendTail(self, value: int) -> None:
        self.tail.append(value)

    def deleteHead(self) -> int:
        if self.head==[]:
            if self.tail==[]:
                return -1
            else:
                while self.tail!=[]:
                    self.head.append(self.tail.pop())
                return self.head.pop()
        else:
            return self.head.pop()
'''

# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()
