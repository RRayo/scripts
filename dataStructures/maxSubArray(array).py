# Given an integer array nums, find the subarray with the largest sum, and return its sum.

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        current_sum = nums[0]

        # recorrer el arreglo, sumando 
        # if find a bigger element than the current sum
        # guardar current sum, actualizar si no da negativo
        # si el resultado da negativo, abandonar ese substring y partir de nuevo con el siguiente elemento no negativo
        # actualizar el max si el current sum es mayor
        #print(nums)
        for n in nums[1:]:
            #print("n",n,"max", max_sum, "current",current_sum)
            # current va a sumar siempre que no encuentre un numero que le gane al conteo actual
            if current_sum + n < n:
                current_sum = n
            else:
                current_sum = current_sum + n
            max_sum = max(max_sum, current_sum)
            #print("max", max_sum, "current",current_sum)

        # [-2,      1,   -3,    4,   -1,    2,   1,    -5,    4]
        # [-2,-2] [1,1] [1,1] [4,4] [3,4] [5,5] [6,6]  [1,6] [5,6]

        return max_sum

s = Solution()

cases = [
    [[-2,1,-3,4,-1,2,1,-5,4], 6],
    [[1], 1],
    [[5,4,-1,7,8], 23],
]

for input, expected in cases:
    result = s.maxSubArray(input)
    print(result == expected, input, result, expected)