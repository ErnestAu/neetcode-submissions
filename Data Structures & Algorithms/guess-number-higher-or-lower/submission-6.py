# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        s = 1
        e = n
        
        while s<e:
            m = (s+e)//2
            res = guess(m)
            if res==-1:
                e=m-1
            elif res == 1:
                s = m+1
            else:
                return m
        return s