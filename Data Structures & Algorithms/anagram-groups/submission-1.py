# [0,0,0,0,0,...]
# [a,b,c,d,e,....] won't have this







class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = defaultdict(list)
        for str in strs:
            check = [0] * 26 #a-z
            for i in str:
                check[ord(i) - ord('a')] += 1
            hashMap[tuple(check)].append(str)

        return hashMap.values()


