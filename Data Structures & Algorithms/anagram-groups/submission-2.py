# iterate
# Counter() on each element





class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}

        for i in range(len(strs)):
            key = [0]*26
            for character in strs[i]:
                key[ord(character) - ord('a')] += 1

            key = tuple(key)

            if key in hashMap:
                hashMap[key].append(strs[i])
            else:
                hashMap[key] = [strs[i]]
        
        return [value for key,value in hashMap.items()]


        # res = []
        # for i in range(len(strs)):
        #     for j in range(i+1,len(strs)):
        #         if Counter(i) == Counter(j):
        #             res