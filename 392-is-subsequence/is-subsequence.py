class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        slow = 0
        c = len(s)
 
        for fast in range(len(t)):
            if slow < len(s) and s[slow] == t[fast]:
                c -= 1
                slow += 1
                if not c:
                    return True



        return False
