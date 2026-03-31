class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        left, right = 0, len(nums) - 1

        while left <= right:
            if nums[left] < nums[right]:
                res = min(res, nums[left])
                break

            mid = (right + left) // 2
            res = min(res, nums[mid])
            if nums[mid] >= nums[left]:
                left = mid + 1
            else:
                right = mid - 1

        return res


"""
  0 1 2 3 4 5
 [3,4,5,6,1,2]
 
 [1,2,3,4,5,6]

 [6,1,2,3,4,5]
 [6,1,2] [3,4,5]
 [6,1] [2]
 [6] [1]

 0 + 5 // 2 =2
 0:2 3:5
"""