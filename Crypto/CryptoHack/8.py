data = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
data=bytes.fromhex(data)
known = b"crypto{"
ct_start=bytes(p^c for c,p in zip(data[:7],known))
print(ct_start)
key = b"myXORkey"
print(bytes(c ^ key[i % len(key)] for i, c in enumerate(data)))



