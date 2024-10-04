from typing import List


class Solution:
       def longestConsecutive(self, nums: List[int]) -> int:
            if len(nums) == 0:
                 return 0
            resultSet = set(nums)          
            max = 1
            for num in nums:
                count = 1
                if (num - 1) not in resultSet and (num + 1) in resultSet:
                    nextNum = num + 1
                    while nextNum in resultSet:
                        count += 1
                        if count > max:
                            max = count
                        nextNum += 1
            return max
            
            
obj = Solution()
# print(obj.longestConsecutive([100,4,200,1,3,2]))
# print(obj.longestConsecutive([0,0]))
print(obj.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))