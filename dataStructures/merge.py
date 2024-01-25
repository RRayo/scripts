def merge(nums1, m: int, nums2, n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    
    i, j, k = 0, 0, 0
    merged = [0] * (m + n)

    while i < m and j < n:
        if nums1[i] <= nums2[j]:
            merged[k] = nums1[i]
            i += 1
        else:
            merged[k] = nums2[j]
            j += 1
        k += 1

    while i < m:
        merged[k] = nums1[i]
        i += 1
        k += 1

    while j < n:
        merged[k] = nums2[j]
        j += 1
        k += 1

    # Copy merged array back to nums1
    nums1[:m + n] = merged


nums1, m, nums2, n = [
[-1,0,0,0,3,0,0,0,0,0,0],
5,
[-1,-1,0,0,1,2],
6,
]
print(nums1, nums2)
merge(nums1, m, nums2, n)
print(nums1)

'''
nums1, m, nums2, n = [
[4,5,6,0,0,0],
3,
[1,2,3],
3,
]
print(nums1, nums2)
merge(nums1, m, nums2, n)
print(nums1)

nums1, m, nums2, n = [
[1,2,3,0,0,0],
3,
[2,5,6],
3,
]
print(nums1, nums2)
merge(nums1, m, nums2, n)
print(nums1)
'''

