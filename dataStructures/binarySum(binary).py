def getSum(a: int, b: int) -> int:
    # 32-bit integer max
    MAX = 0x7FFFFFFF
    # 32-bit interger min
    MIN = 0x80000000
    # mask to get last 32 bits
    mask = 0xFFFFFFFF

    while b != 0:
        # calculate carry
        carry = (a & b) & mask # AND -> bits where both sides has 1's
        # perform addition without carry using XOR
        a = (a ^ b) & mask # XOR -> bits where in one side has 1 and the other 0, or the other way around
        # left shift carry to the next bit position
        b = (carry << 1) & mask # move the carry, to his corresponding position

    # if a is negative, convert it to 32-bit integer
    return a if a <= MAX else ~(a ^ mask)
