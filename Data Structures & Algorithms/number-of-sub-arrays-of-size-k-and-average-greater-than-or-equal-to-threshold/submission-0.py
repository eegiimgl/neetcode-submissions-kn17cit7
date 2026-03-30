class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = 0
        left = 0
        curr_sum = 0
        for i, val in enumerate(arr):
            if i - left + 1 > k:
                curr_sum -= arr[left]
                left += 1
            curr_sum += val
            if i - left + 1 == k and curr_sum / k >= threshold:
                res += 1
        
        return res