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
    if B > 32:
        table[(D,B)] = 2**33
        return 2**33
    if B >= D:
        table[(D,B)] = (2**D)-1
        return table[(D,B)]
    if B == 1:
        table[(D,B)] = D
        return D
    if D == 1:
        table[(D,B)] = 1
        return 1
    table[(D,B)] = maxF(D-1,B) + maxF(D-1, B-1) + 1
    return table[D,B]

def minD(F, B):
    for d in range(1, 200):
        if maxF(d,B) >= F:
            return d
    return -2

def minB(F, D):
    for b in range(1, 33):
        if maxF(D,b) >= F:
            return b
    return -2


if __name__=="__main__":
    main()
