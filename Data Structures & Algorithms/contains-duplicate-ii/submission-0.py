class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dups = set()
        left = 0
        for i, num in enumerate(nums):
            if i - left > k:
                dups.remove(nums[left])
                left += 1
            if num in dups:
                return True
            
            dups.add(num)

        return False
