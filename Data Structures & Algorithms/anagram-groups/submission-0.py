class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        
        for i in strs:
            alphabetMap = [0] * 26 #pseudo map for a-z

            for t in i:
                alphabetMap[ord(t) - ord('a')] += 1

            ans[tuple(alphabetMap)].append(i)


        return ans.values()