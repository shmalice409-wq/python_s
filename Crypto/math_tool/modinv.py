from gcd import gcd
import random

def egcd(a,m):
    xa,ya=1,0
    xb,yb=0,1
    while m:
        q=a//m

        xa,ya,xb,yb=xb,yb,xa-q*xb,ya-q*yb
        a,m=m,a%m
    return a,xa,ya

def modinv(a,m):
    g,x,_=egcd(a,abs(m))
    if g!=1:
        raise ValueError('最大公因子不为1')
    return x%m

if __name__=="__main__":
    random.seed(100)
    for i in range(10000):
        a=random.randint(-10000,10000)
        m=random.randint(-10000,10000)
        if m>0 and gcd(a,m)==1:
            assert pow(a,-1,m)==modinv(a,m)
    


