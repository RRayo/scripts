# https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/


def fun(nums):
    max_1 = max(nums)
    i = nums.index(max_1)
    nums.pop(i)
    max_2 = max(nums)
    return (max_1 - 1) * (max_2 -1)
    

def main():

    assert_cases = [
        [[3,4,5,2],12],
        [[1,5,4,5],16]
    ]
    for var1, expected in assert_cases:
        result = fun(var1)
        print("var1={}, expected={}, result={}"
              .format(var1, expected, result))
        if result != expected:
            print("ERROR")

if __name__ == "__main__":
    main()
