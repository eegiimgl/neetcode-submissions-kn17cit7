class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_amount = 0

        left, right = 0, len(heights) - 1
        while left < right:
            cur_amount = (right - left) * min(heights[left], heights[right])

            max_amount = max(max_amount, cur_amount)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        

        return max_amount