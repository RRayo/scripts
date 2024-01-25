# https://leetcode.com/problems/largest-odd-number-in-string/?envType=daily-question&envId=2023-12-07
def largestOddNumber(num: str) -> str:
    # h1: recorrer string al reves, obtener el sub string hasta ese valor, guardarlo y obtener el maximo de la lista
    for i in range(len(num)-1, -1, -1):
        # si vemos un impar obtener desde el comienzo hasta ese sub string
        if int(num[i]) % 2 == 1:
            return num[:i+1]
    return ""
    

def main():
    assert_cases = [
        ["52","5"],
        ["4206",""],
        ["35427","35427"],
    ]
    for num,  expected in assert_cases:
        result = largestOddNumber(num)
        print("num={}, expected={}, result={}"
              .format(num, expected, result))
        if result != expected:
            print("ERROR")

if __name__ == "__main__":
    main()
