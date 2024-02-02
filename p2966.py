def divideArray(nums, k):
    result = []
    nums.sort()

    if len(nums)%3!=0:
        return []
    
    for i in range(len(nums)//3):
        result.append(nums[3*i:3*i+3])

    for sublist in result:
        if sublist[2]-sublist[0]>k:
            return []

    return result

divideArray([1,3,4,8,7,9,3,5,1], 2)