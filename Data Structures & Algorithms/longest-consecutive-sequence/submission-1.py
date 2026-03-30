class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        _hashset = {}

        for num in nums:
            _hashset[num] = 1

        uniq_arr = list(_hashset.keys())
        uniq_arr.sort()
        print(uniq_arr)

        longest = 0
        counter = 1
        for i in range(1, len(uniq_arr)):
            if uniq_arr[i-1] == uniq_arr[i] - 1:
                counter += 1
            else:
                if longest < counter:
                    longest = counter
                counter = 1
        
        if longest < counter:
            longest = counter

        return longest

