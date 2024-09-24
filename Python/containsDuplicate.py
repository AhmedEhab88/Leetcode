from typing import List, Optional

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        occ = {}
        for num in nums:
          occ[num] = occ.get(num, 0) + 1
          if occ[num] >= 2:
             return True
        return False




obj = Solution()
print(obj.containsDuplicate([1,2,3]))
           
        