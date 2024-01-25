# Given an integer array nums, find a subarray that has the largest product, and return the product.

# The test cases are generated so that the answer will fit in a 32-bit integer.
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0

        max_product = nums[0]
        min_product = nums[0]
        result = max_product
        max_product_arr = [max_product]
        min_product_arr = [min_product]

        for num in nums[1:]:
            # Swap max_product and min_product if num is negative
            if num < 0:
                max_product, min_product = min_product, max_product
                max_product_arr.append("flip")
                min_product_arr.append("flip")

            # Update max_product and min_product for the current position
            max_product = max(num, max_product * num)
            min_product = min(num, min_product * num)

            max_product_arr.append(max_product)
            min_product_arr.append(min_product)

            # Update the overall result
            result = max(result, max_product)
        print("max_product_arr", max_product_arr)
        print("min_product_arr", min_product_arr)
        return result


s = Solution()

cases = [
    # [[2,3,-2,4], 6],
    # [[1], 1],
    # [[-2,0,-1], 0],
    # [[3,-1,4], 4],
    [[1,-2,3-5,4,-7,7,0,-10,2,-3,4,-5], 6]
]

for input, expected in cases:
    result = s.maxProduct(input)
    print(result == expected, input, result, expected)