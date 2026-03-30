class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        for i, height in enumerate(heights):
            if not stack:
                stack.append((i, height))
                continue

            curr_i = i
            while len(stack) > 0 and height <= stack[-1][1]:
                popped_i, popped_height = stack.pop()
                area = (i - popped_i) * popped_height
                max_area = max(max_area, area)
                curr_i = popped_i

            stack.append((curr_i, height))
        
        while len(stack) > 0:
            popped_i, popped_height = stack.pop()
            area = (len(heights) - popped_i) * popped_height
            max_area = max(max_area, area)

        return max_area

            


        

