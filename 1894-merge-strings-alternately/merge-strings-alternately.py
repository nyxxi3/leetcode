class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        #word 1 and word2 as input
        #assign a var (bool) that switches between word1 and word2 and let it access true-> word1 false -> word2
        #put it inside loop, let it run n times where n = min(word1, word2), let merged var take in the chars by pop()
        #end of the loop, look which is empty and add to merged
        toggle = True
        merged = []
        word1 = list(word1)
        word2 = list(word2)  
        while(word1 and word2):
            if toggle:
                merged.append(word1.pop(0))
                toggle = False
            else:
                merged.append(word2.pop(0))
                toggle = True
               
        if word1:
            merged.extend(word1)
        else:
            merged.extend(word2)
        return "".join(merged)
