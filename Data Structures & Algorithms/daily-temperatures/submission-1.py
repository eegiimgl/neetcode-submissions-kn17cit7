class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # (index, temp)
        res = [0] * len(temperatures)

        for i, val in enumerate(temperatures):

            while len(stack) > 0 and stack[-1][0] < val:
                stack_val, stack_i = stack.pop()
                res[stack_i] = i - stack_i
            stack.append((val, i))
        
        return res