# The Computer Language Benchmarks Game
# http://benchmarksgame.alioth.debian.org/
#
# contributed by Rene Bakker
# fixed by Isaac Gouy

from io import StringIO
from gmpy2 import xmpz,div,mul,add

import sys,os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import config

N = int(config.C2_ARG[0])
f = StringIO()

w = xmpz(0)
k = 1

n1  = xmpz(4)
n2  = xmpz(3)
d   = xmpz(1)
f10 = xmpz(10)
n10 = xmpz(-10)

i = 0
while True:
    if int(div(n1, d)) == int(div(n2, d)):
        u = int(div(n1, d))
        f.write(chr(48 + u))
        i += 1
        if i % 10 == 0:
            f.write("\t:%d\n" % i)

        if i == N:
            break

        # extract
        n1 = add(mul(n1, f10), mul(d, mul(n10, u)))
        n2 = add(mul(n2, f10), mul(d, mul(n10, u)))
    else:
        # produce
        n1 = add(mul(n1, (k << 1) - 1), add(n2, n2))
        n2 = add(mul(n1, k - 1), mul(n2, k + 2))
        d = mul(d, (k << 1) + 1)
        k += 1

if i % 10 != 0:
    f.write("%s\t:%d\n" % (' ' * (10 - (i%10)),N))
print(f.getvalue(),end="")