class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest, left = 0, 0
        freq = defaultdict(int)
        for right in range(len(s)):
            freq[s[right]] += 1
            top_freq = max(list(freq.values()))
            while right - left + 1 - top_freq > k:
                freq[s[left]] -= 1
                left += 1
            longest = max(longest, right - left + 1)

        return longest
        
