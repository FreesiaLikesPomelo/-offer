# -*- coding: UTF-8 -*- 

class Solution:
    def replaceSpace(self, s):
        # write code here
        # return s.replace(' ','%20') # 
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
			#print(p_tail," ",p_fwd)
			if(s[p_fwd]==' '):
				#s=s.replace(s[p_tail-2:p_tail],'%20')
				#print(p_tail," ",p_fwd)
				#s[p_tail-2:p_tail]='%20'
				s[p_tail]='0'
				s[p_tail-1]='2'
				s[p_tail-2]='%'
				#print(s)
				p_tail-=3
				p_fwd-=1
				spaceCount -=1
			else:
				s[p_tail]=s[p_fwd]
			    #print(s)
				p_tail-=1
				p_fwd-=1
        return ''.join(s)
    
'''
# below is an example. 
sol=Solution()
s = ' We are  Happy. '
print(sol.replaceSpace(s))
'''
