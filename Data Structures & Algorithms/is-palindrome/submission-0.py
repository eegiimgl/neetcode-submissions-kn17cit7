class Solution:
    def isPalindrome(self, s: str) -> bool:
        def is_valid(c):
            code = ord(c)
            return (48 <= code <= 57) or (65 <= code <= 90) or (97 <= code <= 122)

        left, right = 0, len(s) - 1

        while left < right:
            if not is_valid(s[left]):
                left += 1
            elif not is_valid(s[right]):
                right -= 1
            else:
                if s[left].upper() == s[right].upper():
                    left += 1
                    right -= 1
                else:
                    return False

        return True
            