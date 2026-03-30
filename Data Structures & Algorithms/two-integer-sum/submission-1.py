class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        _hash = {}

        for i,n in enumerate(nums):
            _hash[target-n] = i

        print(_hash)
        
        for i, n in enumerate(nums):
            if n in _hash and i != _hash[n]:
                return [i, _hash[n]]

    