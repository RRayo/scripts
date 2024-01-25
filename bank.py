# https://leetcode.com/problems/calculate-money-in-leetcode-bank/description/
def total_money(n: int) -> int:
    total = 0
    for i in range(0, n):
        extra_week = i//7
        day_saving = i%7 + 1
        total += day_saving + extra_week
    return total

def main():
    n = 10
    total = total_money(n)
    print(total)

if __name__ == "__main__":
    main()
