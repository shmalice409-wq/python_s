"""这道题目是一个综合：
我用一个字节的异或运算隐藏了一些数据，但这个字节是秘密。别忘了先从十六进制解码。
一个比特能包含的数只到256，所以暴力求解就行"""
data = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
data=bytes.fromhex(data)
for k in range(256):
    pt=bytes(b^k for b in data)
    """这里是打印所有的能表示的英文范围的pt"""
    if all(32 <= b < 127 for b in pt):     # 全是可打印 ASCII
        print(k, pt)

