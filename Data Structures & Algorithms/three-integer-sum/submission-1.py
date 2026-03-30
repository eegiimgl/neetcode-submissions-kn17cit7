class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        print(nums)

        i = 0
        N = len(nums)

        res = []
        while i < N-2:
            if i > 0 and nums[i] == nums[i-1]:
                i += 1
                continue

            j = i+1
            k = N-1

            while j < k:
                if nums[j] + nums[k] > -nums[i]:
                    k -= 1
                elif nums[j] + nums[k] < -nums[i]:
                    j += 1
                else:
                    res.append([nums[i],nums[j],nums[k]])
                    j += 1
                    k -= 1
                    while nums[j] == nums[j-1] and j<k:
                        j += 1
        
            i += 1
        
        return res