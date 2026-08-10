def pow_mod(a, b, m):
    """这里是朴素版的快速幂算法，求a^b mod m
    当b=0的时候，很显然a^0 mod m =1
    """
    if b == 0:
        return 1 % m
    sum = 1
    while b:
        sum *= a
        sum %= m
        b -= 1
    return sum % m


def bin_pow(a, b, m):
    """这里是快速幂的为运算求法。算法思路是当要求一个数的多少次方的时候
    我们可以将此数拆成二进制形式，故而此数有若干偶数倍次方相乘得到，所以只有当二进制位为1 的时候才进行相乘。
    用b & 1 来判断最后一位的情况，并且每轮更新基数使得其满足当前位次，当b==0的时候结束。"""
    result = 1
    base = a
    while b:
        if b & 1:
            result = result * base % m
        base = base * base % m
        b >>= 1
    return result % m


import random

if __name__ == "__main__":
    random.seed(100)
    for _ in range(1000):
        a = random.randint(-10000, 10000)
        b = random.randint(0, 1000000)
        m = random.randint(1, 10000)
        assert pow(a, b, m) == bin_pow(a, b, m)
