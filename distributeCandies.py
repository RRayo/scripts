# https://leetcode.com/problems/distribute-candies-to-people/description/

def distributeCandies(candies: int, num_people: int) -> [int]:
    a = [0] * num_people
    accumulated = 0
    for i in range(candies):
        index = i%num_people
        if accumulated + i+1 > candies:
            a[index] += candies - accumulated
            break
        a[index] += i+1
        accumulated += i+1

    return a

def main():
    # 1 <= candies <= 10^9
    # 1 <= num_people <= 1000

    assert_cases = [
        [7,4,[1,2,3,1]],
        [10,3,[5,2,3]],
    ]
    for candies, num_people, expected in assert_cases:
        result = distributeCandies(candies, num_people)
        print("money={}, children={}, expected={}, result={}".format(candies, num_people, expected, result))
        if result != expected:
            print("ERROR")

if __name__ == "__main__":
    main()
