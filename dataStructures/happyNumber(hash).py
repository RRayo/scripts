class Solution:
    def happyFun(self, n):
        return sum(int(digit) ** 2 for digit in str(n))

    def isHappy(self, n: int) -> bool:
        seen_numbers = set()
        
        while n != 1 and n not in seen_numbers:
            seen_numbers.add(n)
            n = self.happyFun(n)
            
        return n == 1
    
###############################################################
    def happyFun(self, n):
        counter = 0
        for l in str(n):
            counter += int(l)**2
        return counter

    def isHappy(self, n: int) -> bool:
        s = set()
        h = self.happyFun(n)
        while(h != 1 and h not in s):
            s.add(h)
            h = self.happyFun(h)
        if h == 1:
            return True
        return False

def main():

    assert_cases = [
        [19,True],
        [2, False],
    ]

    solution = Solution()
    for var1, expected in assert_cases:
        result = solution.isHappy(var1)
        print("var1={}, expected={}, result={}"
              .format(var1, expected, result))
        if result != expected:
            print("ERROR")

if __name__ == "__main__":
    main()