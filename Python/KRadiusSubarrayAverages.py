class Solution:
    def getAverages(self, nums: list[int], k: int) -> list[int]:
        #Form prefix sum array
        prefix = []
        sum = 0
        for num in nums:
            sum += num
            prefix.append(sum)
        arrayLength = len(nums)
        sol = []
        for i in range(0, arrayLength):
            #-1 Cases
            if i < k or ((arrayLength - i) <= k):
                sol.append(-1)
            #Else: calculate 
            else:
                lastIndexLeft = -1
                if i - k - 1 >= 0: 
                    lastIndexLeft = i - k - 1
                leftSum = 0 if lastIndexLeft == -1 else prefix[lastIndexLeft]  
                avg = ((prefix[i] - leftSum) + (prefix[i+k] - prefix[i])) // ((k * 2) + 1)
                sol.append(avg)
        return sol
    

test = Solution()
test1 = [7,4,3,9,1,8,5,2,6]
test2 = [100000]
test3 = [8]
print( test.getAverages(test2, 0)) 