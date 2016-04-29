#!/user/bin/env python
"""Google Code Jam 2008: Problem C. Egg Drop"""

from builtins import input

table = {}

def main():
    N = int(input())
    if N < 1 or N > 100:
        raise RuntimeError("N is not within the valid range")
    for i in range(N):
        F,D,B = map(int, input().split())
        r = EggDrop(F,D,B)
        print("Case #" + str(i + 1) + ": " + r)

def EggDrop(F,D,B):
    f = maxF(D,B)
    if f >= 2**32:
        f = -1
    return ( str(f) + " " + str(minD(F,B)) + " " + str(minB(F,D)))

def maxF(D, B):
    if table.get((D,B), 0) != 0:
        return table[(D,B)]
    if B >= D:
        table[(D,B)] = (2**D)-1
        return (2**D)-1
    if B == 1:
        table[(D,B)] = D
        return D
    table[(D,B)] = maxF(D-1,B) + maxF(D-1, B-1) + 1
    return table[D,B]

def minD(F, B):
    if B == 1:
        return F
    d = 1
    while maxF(d,B) < F:
        d += 1
    return d 

def minB(F, D):
    b = 1
    while maxF(D,b) < F:
        b += 1
    return b


if __name__=="__main__":
    main()
