def sequentialDigits(low, high):
    
    res_list = []
    for i in range(len(str(low)), len(str(high))+1):
        
        arr = [(i+1) for i in range(i)]
        while (arr[len(arr)-1] <= 9):

            num = int(''.join(map(str, arr)))
            if num >= low and num <= high:
                res_list.append(num)
            
            arr = [(i+1) for i in arr]

    return res_list
 

print(sequentialDigits(10, 5000))
