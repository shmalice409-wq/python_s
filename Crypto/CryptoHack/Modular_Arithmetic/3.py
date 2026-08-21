def quick_mod(a,b,p):
    """CryptoHack这道题实际上是让我们学会快速幂，之前实现过快速幂，这里不再赘述

    Args:
        a (int): 底，可以认为是基数
        b (int): 指数
        p (int): 模数

    Returns:
        int: 最后的结果
    """
    result=1
    base=a
    while b:
        if b & 1:
            result=result*base%p
        base=base*base%p
        b>>=1
    return result

print(quick_mod(3,17,17))
print(quick_mod(5, 17, 17))
print(quick_mod(7, 16, 17))
print(quick_mod(273246787654, 65536, 65537))
