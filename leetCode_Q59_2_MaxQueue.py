'''
面试题59 - II. 队列的最大值
请定义一个队列并实现函数 max_value 得到队列里的最大值，要求函数max_value、push_back 和 pop_front 的均摊时间复杂度都是O(1)。
若队列为空，pop_front 和 max_value 需要返回 -1
示例 1：
输入: 
["MaxQueue","push_back","push_back","max_value","pop_front","max_value"]
[[],[1],[2],[],[],[]]
输出: [null,null,null,2,1,2]
示例 2：
输入: 
["MaxQueue","pop_front","max_value"]
[[],[],[]]
输出: [null,-1,-1]
限制：
1 <= push_back,pop_front,max_value的总操作数 <= 10000
1 <= value <= 10^5

执行用时 :296 ms, 在所有 Python3 提交中击败了54.23%的用户
内存消耗 :17 MB, 在所有 Python3 提交中击败了100.00%的用户
'''

class MaxQueue:
    def __init__(self):
        self.que = []
        self.maxQue = []
        self.maxVal = None

    def max_value(self) -> int:
        #print("max_value  ","self.que:",self.que,"self.maxQue:",self.maxQue)
        if self.maxQue==[]:
            return -1
        else:
            return self.maxQue[0]


    def push_back(self, value: int) -> None:
        if self.que==[]:
            self.que.append(value)
            self.maxQue.append(value)
            self.maxVal = value
        else:
            self.que.append(value)
            if self.maxVal<=value:
                self.maxVal = value
                self.maxQue = [value]*len(self.que)
            else:
                # self.maxVal>value
                if self.maxQue[-1]<value:
                    # turn them into value
                    self.maxQue.append(value)
                    n = len(self.maxQue)
                    for i in range(n):
                        if self.maxQue[n-1-i]<=value:
                            self.maxQue[n-1-i]=value
                            #print("self.maxQue:",self.maxQue)
                        else:
                            break
                else:
                    # self.maxQue[-1]>value:
                    self.maxQue.append(value)
        #print("push_back  ","self.que:",self.que,"self.maxQue:",self.maxQue)

    def pop_front(self) -> int:
        if self.que==[]:
            return -1
        else:
            front = self.que.pop(0)
            maxNum = self.maxQue.pop(0)
            if self.maxQue!=[]:
                self.maxVal = self.maxQue[0]
            #print("Pop_front  ","push_back  ","self.que:",self.que,"self.maxQue:",self.maxQue)
            return front

# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()
