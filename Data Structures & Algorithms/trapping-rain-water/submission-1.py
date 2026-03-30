class Solution:
    def trap(self, height: List[int]) -> int:
        N = len(height)
        max_left = [0] * N
        max_right = [0] * N

        cur_max = 0
        for i in range(0, N):
            if i == 0:
                max_left[i] = 0
            else:
                cur_max = max(height[i-1], cur_max)
                max_left[i] = cur_max
        
        cur_max = 0
        for i in range(N-1, 0, -1):
            if i == N-1:
                max_right[i] = 0
            else:
                cur_max = max(height[i+1], cur_max)
                max_right[i] = cur_max
        
        total = 0
        for i in range(0, N):
            cur = min(max_left[i], max_right[i]) - height[i]
            total += 0 if cur < 0 else cur
        
        return total

