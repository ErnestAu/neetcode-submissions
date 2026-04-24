class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        mapS, mapT = {}, {} # key alphabet, value occurence

        for i in range(len(s)):
            mapS[s[i]] = 1 + mapS.get(s[i],0)
            mapT[t[i]] = 1 + mapT.get(t[i],0)
        
        return mapS==mapT



        mapS, mapT = {}, {} # key alphabet, value occurence

        for i in s:
            mapS[i] = 1 + mapS.get(i, 0)

        for i in t:
            mapT[i] = 1 + mapT.get(i, 0)

        return mapS == mapT