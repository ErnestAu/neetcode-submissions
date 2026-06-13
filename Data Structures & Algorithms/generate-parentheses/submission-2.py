class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        

        def backtrack(cur, open_count, close_count):
            if len(cur) == 2*n:
                results.append(cur)
                return
            
            if open_count < n:
                backtrack(cur + "(", open_count+1, close_count)

            if close_count < n and close_count < open_count:
                backtrack(cur + ")", open_count, close_count+1)
        
        
        results = []
        cur = ""

        backtrack(cur, 0, 0)

        return results


    #     cnt ={
    #         "(":n,
    #         ")":n
    #     }
    #     parStr = ""
    #     results = []

        
    #     self.helper(cnt,parStr,results)

    #     return results

    # def helper(self, cnt, parStr, results):
        
        
    #     if cnt["("] == 0 and cnt[")"] == 0:
    #         results.append(parStr)
    #         return

    #     if cnt["("] != 0:

    #         cnt["("] -= 1
    #         self.helper(cnt, parStr +"(", results)
    #         cnt["("]+= 1

    #     if cnt[")"] > cnt["("] and cnt[")"]!=0:

    #         cnt[")"] -= 1
    #         self.helper(cnt, parStr + ")", results)
    #         cnt[")"]+=1
        

        
        
    #     # if cnt[")"] > cnt["("] and cnt[")"]!=0:
    #     #     parStr += ")"
    #     #     cnt[")"] -= 1
    #     #     self.helper(cnt, parStr, results)
    #     # if cnt["("]!=0:
    #     #     parStr += "("
    #     #     cnt["("] -= 1
    #     #     self.helper(cnt, parStr, results)

    #     # if cnt["("] == 0 and cnt[")"] == 0:
    #     #     results.append(parStr)
    #     #     return
