class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ["a","e","i","o","u","A","E","I","O","U"]
        s = list(s)
        v = []
        index = []
        #start with input. make an array to store indexes where vowels was found
        for i,c in enumerate(s):
            if c in vowels:
                v.append(c)
                index.append(i)
        v = list(reversed(v))
        for i in range(len(v)):
            s[index[i]] = v[i]
        return "".join(s)

        