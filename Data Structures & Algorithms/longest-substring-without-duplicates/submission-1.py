class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        seen = {}
        L, R = 0, 0

        while R < len(s):
            if s[R] in seen and seen[s[R]] >= L:
                L = seen[s[R]] + 1
            seen[s[R]] = R
            longest = max(longest, R - L + 1)
            R += 1

        return longest