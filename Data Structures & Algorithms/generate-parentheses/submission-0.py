class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        cnt ={
            "(":n,
            ")":n
        }
        parStr = ""
        results = []

        
        self.helper(cnt,parStr,results)

        return results

    def helper(self, cnt, parStr, results):
        
        
        if cnt["("] == 0 and cnt[")"] == 0:
            results.append(parStr)
            return

        if cnt["("] != 0:

            cnt["("] -= 1
            self.helper(cnt, parStr +"(", results)
            cnt["("]+= 1

        if cnt[")"] > cnt["("] and cnt[")"]!=0:

            cnt[")"] -= 1
            self.helper(cnt, parStr + ")", results)
            cnt[")"]+=1
        

        
        
        # if cnt[")"] > cnt["("] and cnt[")"]!=0:
        #     parStr += ")"
        #     cnt[")"] -= 1
        #     self.helper(cnt, parStr, results)
        # if cnt["("]!=0:
        #     parStr += "("
        #     cnt["("] -= 1
        #     self.helper(cnt, parStr, results)

        # if cnt["("] == 0 and cnt[")"] == 0:
        #     results.append(parStr)
        #     return
