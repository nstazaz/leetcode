class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=defaultdict(list) 
        for l in strs:
            key=[0]*26
            for c in l:
                key[ord(c)-ord("a")]+=1
                #print(key)
            res[tuple(key)].append(l)
        return list(res.values())        
        