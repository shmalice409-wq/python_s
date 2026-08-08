import random
import math


def gcd(a,b):
    a,b=abs(a),abs(b)
    while b:
        a,b=b,a%b
    return a
if __name__ == "__main__":
    for i in range(100):
        a=random.randint(-10000,10000)
        b=random.randint(-10000,10000)

        if math.gcd(a,b) != gcd(a,b):
            print(f'第{i}轮对比出现问题', math.gcd(a,b),gcd(a,b))
            break
    else:
        print('成功实现！')
    print(gcd(0,5))
