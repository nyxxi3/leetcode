class Solution:
    def reverseVowels(self, s: str) -> str:
        #pointers at end and start
        #see if they in vowels. 
        #if both end and start at vowels, swap items in pointers, move to next char
        #else if one of the pointer is in vowel other is not shift only the pointer in non-vowel
        # if both of them not in vowels move pointers
        #release when no chars left anymore (start < end)
        vowels = set("aeiouAEIOU")
        s = list(s)
        start = 0
        end = len(s)-1
        while start < end:
            if s[start] in vowels and s[end] in vowels:
                s[start],s[end] = s[end],s[start]
                start +=1
                end -= 1
            elif s[start] in vowels and s[end] not in vowels:
                end -=1
            elif s[start] not in vowels and s[end] in vowels:
                start += 1
            else:
                start += 1
                end -= 1
        return "".join(s)
