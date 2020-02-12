# -*- coding: UTF-8 -*-
class Solution:			
	def _printNumber(self,StrNum):
		'''
		this fuction is to print the number stored in the sting.
		input: ['0','1','0']
		output: 10
		'''
		#print("print_Number")
		for i in range(len(StrNum)):
			if StrNum[i]!='0':
				print(''.join(StrNum[i:]))
				break
			
	def _printRecursively(self,StrNum, length, idx):
		if idx==length-1:
			#print(idx)
			self._printNumber(StrNum)
		else:	
			idx+=1
			for i in range(10):
				StrNum[idx]='%d' %i
				self._printRecursively(StrNum,length,idx)
		
	def print1ToMaxNDigits(self, n):
		if n<=0:
			print("Invilid Input: n should be an positive integer.")
		
		# store the number.
		StrNum=['0']*n # Store N digits as a string
		length = len(StrNum)
		#print(StrNum)
		for i in range(10):
			StrNum[0]='%d' %i
			self._printRecursively(StrNum,length,0)
		
s=Solution()
s.print1ToMaxNDigits(0)

