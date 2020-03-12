
'''
# 执行用时 :32 ms, 在所有 Python3 提交中击败了85.23%的用户
# 内存消耗 :13.3 MB, 在所有 Python3 提交中击败了100.00%的用户
class Solution:
    def add(self, a:int, b:int)->int:
        nums = [a,b]
        return sum(nums)
'''


# 执行用时 :52 ms, 在所有 Python3 提交中击败了20.62%的用户
# 内存消耗 :13.7 MB, 在所有 Python3 提交中击败了100.00%的用户

#注意:
#由于python不限制数的范围，当异号数相加大于0时，进位为负数，带符号左移时不断变小，因此统一转换为加数相反数#之和，取反。即(a + b) = - (-a + -b)。e.g. a = -3, b = 4, -3 + 4 = -(3 + -4) = -(-1) = 1
class Solution:
    def addPostive(self, a:int, b:int)->int:
        carry = a&b
        carry = carry<<1
        unit = a^b
        if carry==0:
            print("&:",carry,"^",unit)
            return unit^carry
        else:
            print("try again","&:",carry,"^",unit)
            return self.addPostive(unit,carry)

    def add(self, a: int, b: int) -> int:
        if a==0:
            return b
        elif b==0:
            return a
        elif a==-b:
            return 0
        elif a>0 and b>0:
            return -self.addPostive(-a,-b)
        elif a<0 and b<0:
            return self.addPostive(a,b)
        else: 
            # one of a, b is negtive
            if a<0 and -a<b:
                a = -a
                b = -b
                return -self.addPostive(a,b)
            elif b<0 and -b<a:
                a=-a
                b=-b
                return -self.addPostive(a,b)
            else:
                return self.addPostive(a,b)


#s = Solution()
#a = 111
#b = 899
#print(s.add(a,b))
