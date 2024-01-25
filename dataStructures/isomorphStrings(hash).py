from collections import Counter

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # zip both strings, save the relation s[i] -> t[i] in a map ->  if find a new one like s[i] -> t[j] and t[j] != t[i] return false
        if len(s) != len(t):
            return False
        
        char_relations_s_t = {}
        char_relations_t_s = {}
        for i in range(len(s)):
            if s[i] in char_relations_s_t and char_relations_s_t[s[i]] != t[i]:
                return False
            if s[i] not in char_relations_s_t:
                char_relations_s_t[s[i]] = t[i]
            if t[i] in char_relations_t_s and char_relations_t_s[t[i]] != s[i]:
                return False
            if t[i] not in char_relations_t_s:
                char_relations_t_s[t[i]] = s[i]
        return True

def main():

    assert_cases = [
        ["egg","add",True],
        ["foo","bar",False],
        ["paper","title",True],
        ["bbbaaaba","aaabbbba",False],
        ["badc","baba",False],
    ]

    solution = Solution()
    for var1, var2, expected in assert_cases:
        result = solution.isIsomorphic(var1, var2)
        print("var1={}, var2={}, expected={}, result={}"
              .format(var1, var2, expected, result))
        if result != expected:
            print("ERROR")

if __name__ == "__main__":
    main()