k1 = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
k2k1 = "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"
k2k3 = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
fk1k3k2 = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"
"""这里主要是学习异或运算特性
交换律：A ⊕ B = B ⊕ A
结合律：A ⊕ (B ⊕ C) = (A ⊕ B) ⊕ C
单位元：A ⊕ 0 = A
自逆元：A ⊕ A = 0
同时再异或的时候要对所有的十六进制数变成字节才能进行异或
"""
k1=bytes.fromhex(k1)
k2k1=bytes.fromhex(k2k1)
k2k3=bytes.fromhex(k2k3)
fk1k3k2=bytes.fromhex(fk1k3k2)
k2=bytes(x^y for x,y in zip(k1,k2k1))
k3=bytes(x^y for x,y in zip(k2,k2k3))
fk1k3 = bytes(x ^ y for x, y in zip(fk1k3k2, k2))
fk1 = bytes(x ^ y for x, y in zip(fk1k3, k3))
f =  bytes(x ^ y for x, y in zip(fk1, k1))
print(f)
