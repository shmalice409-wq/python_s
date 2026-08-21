def egcd(x, y):
    """拓展欧几里德算法，后面可以用于求模逆。
    这里也是没有考虑全的版本

    Args:
        x (_type_): _description_
        y (_type_): _description_

    Returns:
        _type_: _description_
    """
    xa, ya = 1, 0
    xb, yb = 0, 1
    while y:
        q = x // y
        xa, ya, xb, yb = xb, yb, xa - q * xb, ya - q * yb
        x, y = y, x % y
    return x, xa, ya

def modinv(a,p):
    """这里是求模逆，乘法逆元本质上是a*d mod p 和1同余，所以我们可以通过拓展欧几里得的最终系数，可以决定这个结果
    同时这里的函数求解是不全的，是为了解决题目

    Args:
        a (int): 求a的逆元
        p (int): 模数

    Returns:
        int: a在模p下的逆元
    """
    g,x,_=egcd(a,p)
    return x%p
print(modinv(3,13))

print(121%29)
