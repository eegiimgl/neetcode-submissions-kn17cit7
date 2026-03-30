class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []

        res = [0] * len(temperatures)
        for i, val in enumerate(temperatures):
            while len(stack) > 0 and stack[-1][1] < val:
                node = stack.pop()
                res[node[0]] = i - node[0]
            stack.append([i,val])
        
        return res
                