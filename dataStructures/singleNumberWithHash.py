def singleNumber(nums):
    s = set()
    for n in nums:
        if n in s:
            s.remove(n)
        else:
            s.add(n)
    return s.pop()


l1 = [1,2,1,1,4,5,5,4]
l2 = [1,2,3,4,5,6,7,1,2,3,4,5,6]
l3 = [1]

print("l1: ", singleNumber(l1))
print("l2: ", singleNumber(l2))
print("l3: ", singleNumber(l3))
        
