def egcd(x,y):
    """拓展欧几里德算法，后面可以用于求模逆。
    这里也是没有考虑全的版本

    Args:
        x (_type_): _description_
        y (_type_): _description_

    Returns:
        _type_: _description_
    """
    xa,ya=1,0
    xb,yb=0,1
    while y:
        q=x//y
        xa,ya,xb,yb=xb,yb,xa-q*xb,ya-q*yb
        x,y=y,x%y
    return x,xa,ya

print(egcd(26513,32321))
