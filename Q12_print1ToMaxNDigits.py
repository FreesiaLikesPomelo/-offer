
class Solution:
	def _printNumber(self,StrNum):
		'''
		this fuction is to print the number stored in the sting.
		input: ['0','1','0']
		output: 10
		'''
		for i in range(len(StrNum)):
			if StrNum[i]!='0':
				print(''.join(StrNum[i:]))
				break
				
	def _increment(self,StrNum):
		'''
		add 1 each time it was called
		this function is to simulate the addition of numbers
		when it reached the biggest number, we need to stop
		['0','0','0']->['0','0','1']->...->['9','9','9'] then stop
		carry->
		overflow-> 
		'''
		carry = 0
		overflow = 0
		n = len(StrNum)-1
		
		while n>=0:
			nsum = int(StrNum[n])+carry
			if n == len(StrNum)-1: # the last digit
				nsum+=1
			
			if nsum==10:
				if n==0:
					overflow = 1
				else:
					carry = 1
					StrNum[n]='0'
			
			else:
				StrNum[n] = '%d' %nsum
				break
			n = n-1
		return overflow
		
	def printNNumber(self,n):
		if n<=0:
			return 0
		else:
			N = ['0']*n
			print(N)
			# add 1 and print 1 number each time
			while self._increment(N)==0:
				self._printNumber(N)

s=Solution()
s.printNNumber(5)
	
