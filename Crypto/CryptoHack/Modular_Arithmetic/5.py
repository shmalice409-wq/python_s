"""本节主要是二次剩余的知识点，先对二次剩余进行定义
如果存在一个a^2 mod p 与x同余，我们说一个整数 x 是二次剩余的数，称a是x的平方根"""
p=29
ints=[14,6,11]

for i in range(p):
    if i**2 % p in ints:
        print(i)
