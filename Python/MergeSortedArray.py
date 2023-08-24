from typing import List


# Solved using leetcode solution : https://leetcode.com/problems/merge-sorted-array/solutions/3037315/fully-explained-java-code-with-approach-in-o-m-n-time/
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = m - 1
        j = n - 1
        k = m + n - 1

        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1


obj = Solution()

print(obj.merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))
# print(obj.merge([1], 1, [], 0))
# print(obj.merge([0], 0, [1], 1))
# print(obj.merge([1, 0], 1, [2], 1))
# print(obj.merge([1, 2, 3, 0, 0, 0], 3, [4, 5, 6], 3))
# print(obj.merge([-1, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0], 5, [-1, -1, 0, 0, 1, 2], 6))
# print(obj.merge([2, 0], 1, [1], 1))
# print(obj.merge([-1, 0, 0, 3, 3, 3, 0, 0, 0], 6, [1, 2, 2], 3))
