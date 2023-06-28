import sys


def findLengthOfLCIS(nums: list[int]) -> int:
    max_length = 1
    counter = 1
    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            counter += 1
            if counter > max_length:
                max_length = counter
        else:
            counter = 1
    return max_length


print(findLengthOfLCIS([2, 2, 2, 2, 2]))
