from collections import defaultdict

class Solution:
    def firstUniqChar(self, s: str) -> int:
        # count occurrences
        # get the index of the smaller
        char_position = {}
        
        for i in range(len(s)):
            char = s[i]
            if char not in char_position:
                char_position[char] = i
            else:
                char_position[char] = float('inf')
            
        if char_position:
            position = min(char_position.values())
            if position == float('inf'):
                position = -1
        return position

def main():

    assert_cases = [
        ["leetcode",0],
        ["loveleetcode",2],
        ["aabb",-1],
        ["aadadaad",-1],
    ]

    solution = Solution()
    for var1, expected in assert_cases:
        result = solution.firstUniqChar(var1)
        print("var1={}, expected={}, result={}"
              .format(var1, expected, result))
        if result != expected:
            print("ERROR")

if __name__ == "__main__":
    main()