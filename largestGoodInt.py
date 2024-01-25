# https://leetcode.com/problems/largest-3-same-digit-number-in-string/description/
def fun(num: str) -> str:
    # idea: recorrer de a chunks el string, castear a int y ver si es multiplo de 111, guardando el mayor
    if len(num) < 3:
        return ""
    if len(num) == 3:
        return num if int(num)%111 == 0 else ""
    maxGoodInt = -1
    maxGoodIntStr = ""
    for i in range(len(num)-2):
        n = int(num[i:i+3])
        print(n)
        if n%111 == 0 and n > maxGoodInt:
            maxGoodInt = n
    if maxGoodInt > 0:
        maxGoodIntStr = str(maxGoodInt)
    if maxGoodInt == 0:
        maxGoodIntStr = "000"
    return maxGoodIntStr
    

def main():

    assert_cases = [
        ["1221000", "000"],
        # ["11", ""],
        # ["222", "222"],
        # ["6777133339", "777"],
        # ["2300019", "000"],
        # ["42352338", ""],
    ]
    for num, expected in assert_cases:
        result = fun(num)
        print("num={}, expected={}, result={}"
              .format(num, expected, result))
        if result != expected:
            print("ERROR")

if __name__ == "__main__":
    main()
