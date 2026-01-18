class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ('a','e','i','o','u')
        left = 0
        vowel_count = 0
        max_vcount = 0
        for right in range(len(s)):
            if s[right] in vowels:
                vowel_count += 1
            max_vcount = max(vowel_count,max_vcount)
            if right - left + 1 >= k:
                if s[left] in vowels:
                    vowel_count -= 1
                left += 1
        return max_vcount

            

