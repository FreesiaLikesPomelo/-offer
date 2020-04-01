'''
面试题41. 数据流中的中位数
如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。
例如，
[2,3,4] 的中位数是 3
[2,3] 的中位数是 (2 + 3) / 2 = 2.5
设计一个支持以下两种操作的数据结构：
void addNum(int num) - 从数据流中添加一个整数到数据结构中。
double findMedian() - 返回目前所有元素的中位数。
示例 1：
输入：
["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"]
[[],[1],[2],[],[3],[]]
输出：[null,null,null,1.50000,null,2.00000]
示例 2：
输入：
["MedianFinder","addNum","findMedian","addNum","findMedian"]
[[],[2],[],[3],[]]
输出：[null,null,2.00000,null,2.50000]
限制：
最多会对 addNum、findMedia进行 50000 次调用。
'''


'''
# 执行用时 :4486 ms, 在所有 Python3 提交中击败了5.12%的用户
# 内存消耗 :24.2 MB, 在所有 Python3 提交中击败了100.00%的用户
class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.big = []
        self.small = []
        self.flag = 0 # 1 - the median changed
        self.median = None

    def addNum(self, num: int) -> None:
        blen = len(self.big)
        slen = len(self.small)
        if blen==0:
            # empty list
            self.big.append(num) 
        elif slen==0:
            if num>self.big[0]:
                self.small.append(self.big[0])
                self.big[0]=num
            else:
                self.small.append(num)
        else:
            if self.small[-1]<=num:
                if num<=self.big[0]:
                    if slen<=blen:
                        self.small.append(num)
                    # adjust the lenth, keep 2 lists the same length
                    else:
                        self.big.insert(0,num)
                elif num>self.big[0]:
                    if num>self.big[-1]:
                        self.big.append(num)
                        blen+=1
                    else:
                        for i in range(1,blen):
                            if num<=self.big[i]:
                                self.big.insert(i,num)
                                blen+=1
                                break
                    if blen-slen>=2:
                        temp = self.big.pop(0)
                        self.small.append(temp)
            else: #self.small[-1]>num:
                for i in range(slen):
                    if self.small[i]>=num:
                        self.small.insert(i,num)
                        slen+=1
                        break
                if slen-blen>=2:
                    temp = self.small.pop()
                    self.big.insert(0,temp)
        self.flag = 1
        #print("small",self.small,"big",self.big)
        return

    def findMedian(self) -> float:
        if self.flag==0:
            return self.median
        else:
            slen=len(self.small)
            blen=len(self.big)
            if slen==blen:
                self.median = (self.small[-1]+self.big[0])/2
            elif slen>blen:
                self.median = self.small[-1]
            else:
                self.median = self.big[0]
            self.flag = 0
            #print("small",self.small,"big",self.big,"median",self.median)
            return self.median
'''

# 执行用时 :1428 ms, 在所有 Python3 提交中击败了16.72%的用户
# 内存消耗 :24.2 MB, 在所有 Python3 提交中击败了100.00%的用户
class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.flag = 0 # 1 - the median changed
        self.median = -1

    def addNum(self, num: int) -> None:
        self.data.append(num)
        self.flag = 1
        return

    def findMedian(self) -> float:
        l = len(self.data)
        if l==0:
            return 
        if l==1:
            return self.data[0]
        if self.flag==1:
            self.data.sort()
            if l%2==0:#even
                self.median = (self.data[int(l/2-1)]+self.data[int(l/2)])/2
            else:
                self.median = self.data[int(l/2)]
            self.flag = 0
            return self.median
        else:
            return self.median


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
