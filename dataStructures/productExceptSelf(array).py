# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n
        
        # Calculate prefix products and store in the result array
        prefix_product = 1
        for i in range(n):
            result[i] *= prefix_product
            prefix_product *= nums[i]

        # Calculate suffix products and accumulate in the result array
        suffix_product = 1
        for i in range(n - 1, -1, -1):
            result[i] *= suffix_product
            suffix_product *= nums[i]

        return result

s = Solution()

cases = [
    [[1,2,3,4], [24,12,8,6]],
    [[-1,1,0,-3,3], [0,0,9,0,0]],
    [[1,2], [2,1]],
]

for input, expected in cases:
    result = s.productExceptSelf(input)
    print(result == expected, input, result, expected)