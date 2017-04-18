#!/user/bin/env python
"""Google Code Jam 2008: Problem C. Numbers"""

from __future__ import print_function
from builtins import input
import gmpy2

def main():
    gmpy2.set_context(gmpy2.context())
    gmpy2.get_context().precision = 75
    T = int(input())
    if T < 1 or T > 100:
        raise RuntimeError("T is not within the valid range")
    for i in range(T):
        n = int(input())
        r = Numbers(n)
        print("Case #" + str(i + 1) + ": " + r)

def Numbers(n):
    i = pow(gmpy2.mpfr(3 + gmpy2.sqrt(5)), n)
    #print(i)
    i = int(gmpy2.rint_trunc(i)) % 1000
    o = i - ((i // 10) * 10)
    t = (i - ((i // 100) * 100) - o) / 10
    h = (i - t - o) / 100
    return str(h)+str(t)+str(o)

if __name__=="__main__":
    main()
