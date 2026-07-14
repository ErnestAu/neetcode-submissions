class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        temp1 = [0] * 26
        temp2 = [0] * 26
        for i in s:
            temp1[ord(i)-ord('a')]+=1
        for i in t:
            temp2[ord(i)-ord('a')]+=1



        return temp1 == temp2