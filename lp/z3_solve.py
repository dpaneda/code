from z3 import *
import random

BITS=32
M = 2**BITS-1

def c_mul(a, b):
    return (long(a) * b) & M

def pyhash(self, prefix, suffix):
    if not self:
        return 0 # empty
    value = prefix
    value ^= ord(self[0]) << 7
    for char in self:
        value = c_mul(1000003, value) ^ ord(char)
    value ^= len(self)
    value ^= suffix

    return value

def zpyhash(self, prefix, suffix):

    value = prefix
    value ^= self[0] << 7

    for char in self:
        value = (1000003*value) ^ char

    value ^= len(self)
    value ^= suffix

    return value

def solve(values):
    prefix = BitVec('prefix', BITS)
    suffix = BitVec('suffix', BITS)

    s = Solver()

    for l, h in values:
        s.add(zpyhash(l, prefix, suffix) == h)

    if s.check() == sat:
        print s.model()

        p = s.model()[prefix].as_long()
        s = s.model()[suffix].as_long()

        return p, s

    raise ValueError

def findcol(x, pr, su, n):
    sol = [BitVec('sol%d'%i, 32) for i in range(n)]

    s = Solver()

    h = zpyhash(sol, BitVecVal(pr, BITS), BitVecVal(su, BITS))

    s.add(h == x)

    for i in range(n):
        s.add(sol[i] < 256)
        s.add(sol[i] >= 0)

    if s.check() == sat:
        val = [s.model()[sol[i]].as_long() for i in range(n)]
        return ''.join(map(chr, val))

    return ''


if __name__ == '__main__':
    random.seed(0x12345678)

    testprefix, testsuffix = random.getrandbits(BITS), random.getrandbits(BITS)

    print testprefix, testsuffix

    print hash('a')&M, pyhash('a', 0, 0), pyhash('a', testprefix, testsuffix)

    values = []

    for i in range(10):
        h = pyhash(chr(i), testprefix, testsuffix)
        values.append(([i], h))

        h = pyhash(chr(i)*2, testprefix, testsuffix)
        values.append(([i]*2, h))


    p, s = solve(values)

    print pyhash('hello', testprefix, testsuffix), pyhash('hello', p, s)
    print pyhash('you_want_it_LOLOLOL?', testprefix, testsuffix), pyhash('you_want_it_LOLOLOL?', p, s)

    h = pyhash('you_want_it_LOLOLOL?', testprefix, testsuffix)
    col = findcol(h, p, s, 8)
    assert (pyhash(col, testprefix, testsuffix) == h)
    print col
    print ':)'
