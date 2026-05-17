# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        start = 1
        end = n
        
        while (start < end):
            num = (start + end)//2
            if guess(num) < 0:
                end = num - 1
            elif guess(num) > 0:
                start = num + 1
            else:
                return num
        return start