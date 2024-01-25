def removeDuplicates(nums) -> int:
    counter = len(nums)
    last_seen = None
    i = 0
    while i < len(nums):
        n = nums[i]
        if n == last_seen and n != '_':
            nums.pop(i)
            nums.append('_')
            counter -= 1
        else:
            last_seen = n
            i += 1
    return counter


nums = [0,0,1,1,1,2,2,3,3,4]

print(nums)
print(removeDuplicates(nums))
print(nums)
