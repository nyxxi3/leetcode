class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #create a set to keep track of characters in the substring
        # left pointer = 0
        # right pointer in the loop
        #max_len = 0
        char_set = set()
        left = 0
        max_len = 0
        for right in range(len(s)):
    #either the char is already in the substring
    # we are going to remove the chars in the set until the old char is removed from the set.
    # shift left  = left + 1
    # it doesnt
    #add the character to the set
    # max_len = max(max_len, right - left + 1)
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            max_len = max(max_len,right-left+1)
        return max_len

                
