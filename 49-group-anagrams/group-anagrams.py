class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #loop
        #compute alphabet list (a frequency array)
        #convert that into a tuple
        #use the tuple as a hashmap key
        #use the words as values (create new key if tuple doesnt exist in hashmap, if exists create new)
        op = []
        a = [0]*26
        
        hashmap = {}
        for str in strs:
            for c in str:
                a[ord(c)-ord('a')] += 1
            if tuple(a) not in hashmap:
                hashmap[tuple(a)] = [str]
            else:
                hashmap[tuple(a)] += [str]
            a = [0]*26
        for v in hashmap.values():
            op.append(v)
        return op
            




