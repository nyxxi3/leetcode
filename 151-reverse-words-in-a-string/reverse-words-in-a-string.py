class Solution:
    def reverseWords(self, s: str) -> str:
        words = []
        current = []
        
        # 1. Manually split into words
        for ch in s:
            if ch != ' ':
                current.append(ch)
            else:
                if current:
                    words.append("".join(current))
                    current = []
        
        # last word
        if current:
            words.append("".join(current))
        
        # 2. Reverse the list of words manually
        left, right = 0, len(words) - 1
        while left < right:
            words[left], words[right] = words[right], words[left]
            left += 1
            right -= 1
        
        # 3. Manually join words back into a string
        res = ""
        for i in range(len(words)):
            res += words[i]
            if i < len(words) - 1:
                res += " "
        
        return res
