'''
test cases:
[] & [] return true
[] & [!] return false
[1] & [] return true

'''

class Solution(object):
    def validate(self, pushed, popped):
        ''' 
        to check two list with same numbers of elements
        :type pushed: List[int] cannot be empty
        :type popped: List[int] cannot be empty
        :rtype: bool
        '''
        stack = []
        pushidx = 0
        popidx = 0
        count = 0
        while pushidx<len(pushed) and popidx<len(popped):
            #print("count: ",count, "pushidx",pushidx,pushed[pushidx],"popidx",popidx,popped[popidx],"stack:",stack)
            # compare pop with stack
            if stack!=[] and stack[-1]==popped[popidx]:
                stack.pop()
                popidx+=1
                #print("delete from stack")
            # compare pop with pushed
            elif pushed[pushidx]==popped[popidx]:
                #print("pushXpop,popidx+1,pushidx+1")
                pushidx+=1
                popidx+=1
            else:
                #print("push!=pop,stack+1,pushidx+1")
                stack.append(pushed[pushidx])
                pushidx+=1
            count+=1
            #print("stack: ", stack)
        if stack==[]:
            return True
        else:
            for i in range(len(popped)-1-popidx):
                if stack!=[] and stack[-1]==popped[popidx]:
                    stack.pop()
                    popidx+=1
                    #print("delete from stack")
                else: 
                    return False
            return True


    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        if popped==[]:
            return True
        else:
            if pushed==[]:
                return False
            else: # function test
                if len(pushed)!=len(popped):# if they contain different numbers of elements
                    return False
                result = self.validate(pushed, popped)
                return result

#s = Solution()
#a = [2,1,0]
#b = [1,2,0]
#a = [1,2,3,4,5]
#b = [4,5,3,2,1]
#print(s.validateStackSequences(a,b))
