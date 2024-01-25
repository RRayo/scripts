def removeElement( nums, val: int) -> int:
    # remove elements in place with value val
    # return k, number of elements different than val
    filtered_arr = []
    for n in nums:
        if n != val:
            filtered_arr.append(n)
    
    j = k = len(filtered_arr)
    while j < len(nums):
        filtered_arr.append('_')
        j += 1
    nums[:len(nums)] = filtered_arr
    return k


nums, val = [3,2,2,3],3
print(nums)
print(removeElement( nums, val))
print(nums)


nums = [0,1,2,2,3,0,4,2]
val = 2

print(nums)
print(removeElement( nums, val))
print(nums)