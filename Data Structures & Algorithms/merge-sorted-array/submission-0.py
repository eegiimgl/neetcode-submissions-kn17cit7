class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        i = len(nums1) - 1
        left, right = m - 1, n - 1

        while left >=0 or right >= 0:
            if left < 0:
                nums1[i] = nums2[right]
                right -= 1
            elif right < 0:
                nums1[i] = nums1[left]
                left -= 1
            elif nums1[left] > nums2[right]:
                nums1[i] = nums1[left]
                left -= 1
            else:
                nums1[i] = nums2[right]
                right -= 1
            i -= 1

        