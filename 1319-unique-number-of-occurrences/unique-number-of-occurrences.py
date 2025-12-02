class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dic = {}
        for i,e in enumerate(arr):
            if e not in dic:
                dic[e] = 1
            else:
                dic[e] += 1
        u = set(dic.values())
        
        return (len(u) == len(dic.values()))

            
