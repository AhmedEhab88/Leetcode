from typing import List
    
def threeSum(nums: List[int]) -> List[List[int]]:
  sol = []
  nums.sort()
  
  for i, a in enumerate(nums):
    if i > 0 and a == nums[i - 1]:
      continue

    l, r = i + 1, len(nums) - 1
    while l < r:
      sum = a + nums[l] + nums[r]
      if sum > 0:
        r -= 1
      elif sum < 0:
        l += 1
      else: 
        sol.append([a,nums[l], nums[r]])
        l += 1
        while nums[l] == nums[l - 1] and l < r:
          l += 1
  return sol



print(threeSum([-1,0,1,2,-1,-4]))