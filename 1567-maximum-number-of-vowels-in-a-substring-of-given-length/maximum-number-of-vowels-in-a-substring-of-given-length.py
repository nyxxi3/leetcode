class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ['a','e','i','o','u']
        max_count = sum(1 for v in s[:k] if v in vowels)
        left = 0
        right = k
        count = max_count
        while right < len(s):
            if s[left] in vowels:
                count -= 1
            if s[right] in vowels:
                count += 1
            max_count = max(count,max_count)
            left += 1
            right += 1
        return max_count
            
        