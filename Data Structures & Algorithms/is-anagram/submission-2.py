class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = list(s)
        s.sort()
        t = list(t)
        t.sort()

        if len(s) != len(t):
            return False

        for i, _ in enumerate(s):
            if s[i] != t[i]:
                return False
        
        return True