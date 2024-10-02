from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1:
            return nums
        #initilization
        count = {}
        res=[]
        buckets = [[] for _ in range(len(nums)+1)]
        
        #Counting occurences of each element
        for n in nums:
            count[n] = count.get(n, 0) + 1
        
        #{1: 3, 2: 2, 3: 1} --> [[3], [2], [1], [], [], []]
        #Adding element to bucket[<count_of_element>]
        for key in count:
            buckets[count[key]].append(key)
        
        #Looping through buckets in reverse to get final result
        for i in range(len(buckets)-1, 0, -1):
            if len(buckets[i]) == 0:
                continue
            else:
                while len(buckets[i]) > 0 and len(res) <= k:
                    res.append(buckets[i].pop())
                if len(res) == k:
                    return res
        return res        

obk = Solution()
print(obk.topKFrequent([-1, -1], 1)) 

## Solution is O(N)
        