def removeElement( nums, val: int) -> int:
    # remove elements in place with value val
    # return k, number of elements different than val
    counter = 0
    i = 0
    while i < len(nums):
        n = nums[i]
        if n == val:
            nums.pop(i)
            nums.append('_')
        else:
            if n != '_':
                counter += 1
            i += 1
    return counter


nums, val = [3,2,2,3],3
print(nums)
print(removeElement( nums, val))
print(nums)


nums = [0,1,2,2,3,0,4,2]
val = 2

print(nums)
print(removeElement( nums, val))
print(nums)