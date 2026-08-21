def gcd(x,y):
    """最大公因子gcd
    这里其实没有考虑到负数和0的情况，这里只是为了解决CryptoHack中的题目
    Args:
        x (int):
        y (int):

    Returns:
        int: 最大公因子
    """
    while y:
        x,y=y,x%y
    return x

print(gcd(66528,52920))

