def findDifference(nums1: list[int], nums2: list[int]) -> list[list[int]]:
    #Creating two dictionaries for each list
    set1, set2 = {}, {}
    i = 0
    for num in nums1: 
        set1[num] = i
        i += 1
    i = 0
    for num in nums2: 
        set2[num] = i
        i += 1
    
    # --- Finding the difference between the two lists --- #
    diff1 = []
    diff2 = []
    #Convert list to dictionary to remove any duplicates from the list, 
    #then convert to list again to loop over it 
    for num in list(dict.fromkeys(set1)):
        if(num not in set2):
            diff1.append(num)
    
    for num in list(dict.fromkeys(set2)):
        if(num not in set1):
            diff2.append(num)
    
    return [diff1, diff2]

def main():
    set1 = [1,2,3,3]
    set2 = [1,1,2,2]

    res = findDifference(set1, set2)
    print(res)

main()