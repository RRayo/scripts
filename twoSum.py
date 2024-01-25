# https://leetcode.com/problems/two-sum/

# https://leetcode.com/problems/distribute-candies-to-people/description/

def twoSum(nums: [int], target: int) -> [int]:
    # logic n1 + n2 = target -> target - n1 = n2
    # transform the array to a dict with key=value, value=position
    d = {}
    for i in range(len(nums)):
        if nums[i] not in d:
            d[nums[i]] = []
        d[nums[i]].append(i)
    for key, val in d.items():
        n2 = target - key
        if n2 in d:
            if key == n2:
                if len(val) == 1: # dont use the same
                    continue
                return [val[0], val[1]]
            return [val[0], d[n2][0]]  
    

def main():
    # 2 <= nums.length <= 10^4
    # -10^9 <= nums[i] <= 10^9
    # -10^9 <= target <= 10^9

    assert_cases = [
        [[2,7,11,15], 9, [0,1]],
        [[3,2,4], 6, [1,2]],
        [[2,5,5,11], 10, [1,2]],
    ]
    for nums, target, expected in assert_cases:
        result = twoSum(nums, target)
        print("numbs={}, target={}, expected={}, result={}".format(nums, target, expected, result))
        if result != expected:
            print("ERROR")

if __name__ == "__main__":
    main()
