class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
        














        
        
        
        
        # if len(s) != len(t):
        #     return False

        # count = [0] * 26
        
        # for i in range(0,len(s)):
        #     count[ord(s[i])-ord('a')] += 1
        #     count[ord(t[i])-ord('a')] -= 1

        # for val in count:
        #     if val != 0:
        #         return False


        # if len(s) != len(t):
        #     return False

        # hashS, hashT = {}, {}
        
        # for i in range(0,len(s)):
        #     hashS[s[i]] = 1 + hashS.get(s[i], 0)
        #     hashT[t[i]] = 1 + hashT.get(t[i], 0)


        # return hashS == hashT



        



        # if len(s) != len(t):
        #     return False
        
        # return sorted(s) == sorted (t)