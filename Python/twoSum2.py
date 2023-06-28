class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        p1 = 0
        p2 = 1
        sol = []
        while p1 < len(numbers):  
            amountLeft = target - numbers[p1]
            #Binary Search on the rest
            left = p2
            right = len(numbers) - 1
            while(left <= right):
                mid = (left + right) // 2
                if(numbers[mid] == amountLeft):
                    sol.append(p1 + 1)
                    sol.append(mid + 1)
                    return sol
                elif numbers[mid] > amountLeft:
                    right = mid  - 1
                else: 
                    left = mid + 1
            p1 += 1
            p2 = p1 + 1
        return sol        
    

test = Solution()

print(test.twoSum([-1,0], -1))