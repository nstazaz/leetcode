class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=dict()
        snn=0
        ths=set()
        for x in nums:
            if x in count:
                count[x]+=1
            else:
                count[x]=1
        print(count)
        for h in range(k):    
            #print(f"done{ths},{snn}")
            snn=0
            for x in count:
                for t in range(1):
                    if snn in ths:
                        snn=x
                    if x in ths:
                        break
                    if snn not in count:
                        snn=x
                    if count[x] > count[snn]:
                        snn=x
            if snn not in ths:
                ths.add(snn)
        #print(ths)                
        return list(ths) 