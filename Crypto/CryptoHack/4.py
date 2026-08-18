from Crypto.Util.number import *
"""这里是将大整数变成字节串"""
s = 11515195063862318899931685488813747395775516287289682636499965282714637259206269
print(long_to_bytes(s))
"""同样的在这个包中存在一个函数bytes_to_long将字节串变成大整数"""
print(bytes_to_long(b'hello'))
