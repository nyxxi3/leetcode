class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s = list(s)
        t=list(t)
        slow = 0
        c = len(s)
        if not s:
            return True
        for fast in range(len(t)):
            if slow < len(s) and s[slow] == t[fast]:
                c -= 1
                slow += 1
                if not c:
                    return True



        return False
