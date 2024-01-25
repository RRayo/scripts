def duplicateZeros(arr) -> None:
    aux = list(arr)
    shifted = 0
    for index, element in enumerate(aux):
        if index + shifted >= len(aux):
            break
        arr[index+shifted] = element

        if element == 0 and index+shifted+1 < len(arr):
            arr[index+shifted+1] = element
            shifted += 1


l1 = [0,2,3,4] # [0,0,2,3]
l2 = [0,2,0]
l3 = [0]

print(l1)
duplicateZeros(l1)
print("l1: ", l1)
print(l2)
duplicateZeros(l2)
print("l2: ", l2)
print(l3)
duplicateZeros(l3)
print("l3: ", l3)
        
