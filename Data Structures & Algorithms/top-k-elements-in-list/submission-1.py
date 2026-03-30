class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)

        for num in nums:
            freq[num] += 1
        

        min_heap = []
        heapq.heapify(min_heap)

        for key, value in freq.items():
            heapq.heappush(min_heap, (value, key))

            if len(min_heap) > k:
                heapq.heappop(min_heap)

        res = []

        for node in min_heap:
            res.append(node[1])

        return res
