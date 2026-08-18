def xor_string(s,key):
    """这个函数实现的是CryptoHack中的XOR启动器，实际上是用来了解XOR允许算的。
    异或运算，本质上是二进制运算，所以我们没有必要可刻意去转换进制，直接使用 ^ 符号即可
    字符串运算的时候要变成ACILL码之后，再运算，这里要求是对每一个字符都要和13异或，然后输出异或之后的字符

    Args:
        s (string): 输入的字符
        key (int): 要进行异或的数字

    Returns:
        _type_: 返回最后组成的字符串
    """
    result=[]
    for c in s:
        result.append(chr(ord(c)^key))
    print(result)
    return ''.join(result)

if __name__=="__main__":
    s='label'
    key=13
    new_string=xor_string(s,key)
    print(f"crypto{{{new_string}}}")
