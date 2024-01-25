# https://leetcode.com/problems/distribute-money-to-maximum-children/description/
def dist_money(money: int, children: int) -> int:
    exact_amount = 8
    restriction = 4
    money = money - children # Todos tienen al menos $1
    if money < 0: # no alcanzaba para todos
        return -1
    exact_amount -= 1 # ahora buscamos los que tienen $7 (ya que ya tienen $1)
    restriction -= 1

    posible_total = money // exact_amount # cuantos podrian alcanzar
    excess = money % exact_amount 

    total = min(posible_total, children)

    if posible_total > children:
        total -= 1
    # restriccion que nadie quede con $4
    if children - posible_total == 1 and excess == restriction:
        total -= 1
    if posible_total == children and excess != 0:
        total -= 1
    return max(total,0)

def main():
    # 1 <= money <= 200
    # 2 <= children <= 30

    assert_cases = [
        [20,3,1],
        [23,2,1],
        [16,2,2],
        [13,3,1],
        [5,3,0],
        [1,2,-1],
        [16,16,0],
        [17,2,1]
    ]
    for money, children, expected in assert_cases:
        result = dist_money(money, children)
        print("money={}, children={}, expected={}, result={}".format(money, children, expected, result))
        if result != expected:
            print("ERROR")

if __name__ == "__main__":
    main()
