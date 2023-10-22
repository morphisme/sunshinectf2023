from Crypto.Util.number import long_to_bytes
import codecs

def translate(c, u):
    return chr((ord(c) - ord('a') + u) % 26 + ord('a'))

ct0 = open('BeepBoop', 'r').read()
ct1 = '0b' + ct0[:-1].replace('beep', '0').replace('boop', '1').replace(' ', '')
ct2 = int(ct1, 2)
pt0 = codecs.decode(long_to_bytes(ct2))[1:]
shift = ord('s') - ord('f')
pt1 = ''.join([c if c in ['{', '-', '}'] else translate(c, shift) for c in pt0])
print(pt1)
