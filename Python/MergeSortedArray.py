from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        if n == 0:
            return nums1
        if m == 0:
            i = 0
            while i < len(nums2):
                nums1.insert(i, nums2[i])
                nums1.pop()
                i += 1
            return nums1

        i, j = 0, 0  # i for nums1, j for num2
        while i < m and j < n:
            if nums1[i] >= nums2[j]:
                nums1.insert(i, nums2[j])
                i += 2
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
        if i > m:
            i = m
            while i < len(nums1) and j < n:
                nums1.insert(i, nums2[j])
                i += 1
                j += 1

        for x in range(0, n):
            nums1.pop()
        return nums1


obj = Solution()

# print(obj.merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))
# print(obj.merge([1], 1, [], 0))
# print(obj.merge([0], 0, [1], 1))
# print(obj.merge([1, 0], 1, [2], 1))
# print(obj.merge([1, 2, 3, 0, 0, 0], 3, [4, 5, 6], 3))
print(obj.merge([-1, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0], 5, [-1, -1, 0, 0, 1, 2], 6))
# print(obj.merge([2, 0], 1, [1], 1))
# print(obj.merge([-1, 0, 0, 3, 3, 3, 0, 0, 0], 6, [1, 2, 2], 3))
