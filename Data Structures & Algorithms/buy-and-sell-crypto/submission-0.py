class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_prof = 0
        left, right = 0, 0

        for right in range(len(prices)):
            if prices[left] > prices[right]:
                left = right
            
            max_prof = max(max_prof, prices[right] - prices[left])

        return max_prof