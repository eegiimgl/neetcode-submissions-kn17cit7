# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:

        def merge_sort(pairs, left, right):
            if right - left + 1 <= 1:
                return pairs
            
            mid = (right + left) // 2

            merge_sort(pairs, left, mid)
            merge_sort(pairs, mid+1, right)

            merge(pairs, left, mid, right)

            return pairs
        
        def merge(pairs, left, mid, right):
            left_arr = pairs[left : mid+1]
            right_arr = pairs[mid+1 : right+1]
            
            i = left
            l, r = 0, 0

            while l < len(left_arr) or r < len(right_arr):
                if l >= len(left_arr):
                    pairs[i] = right_arr[r]
                    r += 1
                elif r >= len(right_arr):
                    pairs[i] = left_arr[l]
                    l += 1
                elif left_arr[l].key <= right_arr[r].key:
                    pairs[i] = left_arr[l]
                    l += 1
                else:
                    pairs[i] = right_arr[r]
                    r += 1
                i += 1

        return merge_sort(pairs, 0, len(pairs)-1)