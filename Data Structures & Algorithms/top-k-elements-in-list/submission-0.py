class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)

        for num in nums:
            freq[num] += 1

        values = list(freq.values())
        values.sort(reverse = True)

        threshold = values[k:]
        threshold_num = 0 if not threshold else threshold[0]
        
        result = []
        for key, value in freq.items():
            if value > threshold_num:
                result.append(key)

        return result