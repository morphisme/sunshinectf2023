# first decompile dill.cpython-38.pyc with uncompyle6
ct0 = 'bGVnbGxpaGVwaWNrdD8Ka2V0ZXRpZGls'
o = [5, 1, 3, 4, 7, 2, 6, 0]
pt = 'sun{'
for j in range(8):
    i = o.index(j)
    pt += ct0[4*i:4*i+4]
pt += '}'
print(pt)
