class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data=[]
        self.minData=[] # to store the min 

    def push(self, x):
        """
        to add a number to the stack, and add min to minData
        :type x: int
        :rtype: None
        """
        if x==None: # push empty element, do nothing
            return None

        if self.data==[]: # now the stack is empty, we need to push it in both two lists
            self.data.append(x)
            self.minData.append(x)
        else:
            self.data.append(x)
            temp = self.minData.pop()
            self.minData.append(temp)
            if temp>x:
                self.minData.append(x)
            else:
                self.minData.append(temp)
            # print(self.minData)
        return None


    def pop(self):
        """
        to delete the toppest number in the stack
        :rtype: None
        """
        if self.data==[]: # empty stack cannot pop anything
            return None
        else:
            data = self.data.pop()
            m = self.minData.pop()
            return None



    def top(self):
        """
        to show the toppest number in the stack, but not delete it
        :rtype: int
        """
        if self.data==[]:
            return None
        else:
            temp = self.data.pop()
            self.data.append(temp)
            return temp

    def min(self):
        """
        to return the min number in the stack, but not delete it
        :rtype: int
        """
        if self.data==[]:
            return None
        else:
            m = self.minData.pop()
            self.minData.append(m)
            return m



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()
