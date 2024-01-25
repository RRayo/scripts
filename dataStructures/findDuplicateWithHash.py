def findDuplicate(numbers):
    s = set()
    for n in numbers:
        if n in s:
            return True
        else:
            s.add(n)
    return False


l1 = [1,2,3,1,4,5,6,7]
l2 = [1,2,3,4,5,6,7]
l3 = [1,2,3,4,5,6,7,1]

print("l1 has duplicate?: ", findDuplicate(l1))
print("l2 has duplicate?: ", findDuplicate(l2))
print("l3 has duplicate?: ", findDuplicate(l3))
        
