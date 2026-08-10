

class Solution:
    def isValid(self, s: str) -> bool:


        res = []

        closes = {
            ")":"(",
            "}":"{",
            "]":"["
        }
        for p in s:
            # if p in opens:
            #     opens[p]+=1
            if p in closes:
                if res and res[-1] == closes[p]:
                    res.pop()
                else:
                    return False
            else:
                res.append(p)

        return not bool(res)