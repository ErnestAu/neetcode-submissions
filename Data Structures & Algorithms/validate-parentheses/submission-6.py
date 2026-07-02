# Input: s = "[]"

# Output: true
# Example 2:

# Input: s = "([{}])"

# Output: true
# Example 3:

# Input: s = "[(])"

# Output: false
class Solution:
    def isValid(self, s: str) -> bool:
        par = {"(": ")", "{": "}", "[": "]"}
        stack = []
        for i in s:
            if i in par:
                stack.append(i)
            else:
                if not stack:
                    return False
                elif i == par[stack.pop()]:
                    continue
                else:
                    return False
        return not stack