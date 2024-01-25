
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def lst2link(lst):
    cur = dummy = ListNode(0)
    for e in lst:
        cur.next = ListNode(e)
        cur = cur.next
    return dummy.next
def link2lst(link):
    lst = []
    while link:
        lst.append(link.val)
        link = link.next
    return lst

class Solution:
    def add(self, l1, l2, aux):
        if not l1 and not l2 and aux == 0:
            return None
        l1_val = l1.val if l1 else 0
        l2_val = l2.val if l2 else 0
        val = aux + l1_val + l2_val
        aux = val // 10
        val = val % 10
        l1_next = l1.next if l1 else None
        l2_next = l2.next if l2 else None
        return ListNode(val, self.add(l1_next, l2_next, aux))
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        return self.add(l1, l2, 0)
    
    def fun(l1, l2):
        # pasar las listas a string, invertirla, pasar a int, sumar ambas,
        # pasar a string, invertirla, pasar a array
        int_l1 = int(''.join(map(str, l1))[::-1])
        int_l2 = int(''.join(map(str, l2))[::-1])
        str_res = str(int_l1+int_l2)[::-1]
        return [int(char) for char in str_res]
    

def main():

    assert_cases = [
        [[2,4,3],[5,6,4],[7,0,8]],
        [[0],[0],[0]],
        [[9,9,9,9,9,9,9],[9,9,9,9],[8,9,9,9,0,0,0,1]],
    ]
    for var1, var2, expected in assert_cases:
        var1 = lst2link(var1)
        var2 = lst2link(var2)

        result = link2lst(Solution().addTwoNumbers(var1, var2))
        print("var1={}, var2={}, expected={}, result={}"
              .format(var1, var2, expected, result))
        if result != expected:
            print("ERROR")

if __name__ == "__main__":
    main()
