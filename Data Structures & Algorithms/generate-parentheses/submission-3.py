class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        arr = [n, n]
        par = ""
        results = []

        def helper(arr, par):
            if arr[0] == 0 and arr[1] == 0:
                results.append(par)
                return
            
            if arr[0] != 0:
                arr[0] -= 1
                helper(arr, par + "(")
                arr[0] += 1
            
            if arr[1] > arr[0] and arr[1] != 0:
                arr[1] -= 1
                helper(arr, par + ")")
                arr[1] += 1
        helper(arr,par)

        return results