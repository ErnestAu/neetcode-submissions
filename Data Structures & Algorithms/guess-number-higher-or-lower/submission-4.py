# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:

        
        def _guessNumber(l, r):
            myguess = (l+r)//2
            res = guess(myguess)
            if res == 1:
                myguess = _guessNumber(myguess + 1, r)
            elif res == -1:
                myguess = _guessNumber(l, myguess - 1)
            return myguess
        
        return _guessNumber(1, n)


        # myguess = n // 2
        
        # if guess:
            