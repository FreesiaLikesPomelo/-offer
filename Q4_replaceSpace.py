
class Solution:
    def replaceSpace(self, s):
        # write code here
        # return s.replace(' ','%20') # then it's done
        spaceCount = 0
        #print(len(s))
        if(len(s)==0):
            return s
        for i in range(len(s)):
            if(s[i]==' '):
                spaceCount+=1
        p_tail = len(s)+2*spaceCount-1
        p_fwd = len(s)-1
        s = s+2*spaceCount*' '
        #print(len(s))
        s = list(s)
        #print(len(s))
        while(spaceCount>0):
            if(s[p_fwd]==' '):
                #s=s.replace(s[p_tail-2:p_tail],'%20') # str.replace('x','O') will replace all 'x' in str. 
                #s[p_tail-2:p_tail]='%20' # the index doesn't need to be checked... it might extend the list
                s[p_tail]='0'
                s[p_tail-1]='2'
                s[p_tail-2]='%'
                p_tail-=3
                p_fwd-=1
                spaceCount -=1
            else:
                s[p_tail]=s[p_fwd]
                p_tail-=1
                p_fwd-=1
        return ''.join(s)
    

'''
# below is an example. 
sol=Solution()
s = ' We are  Happy. '
print(sol.replaceSpace(s))
'''
