#!/user/bin/env python
"""Google Code Jam 2017: Problem B. Ratatouille"""

from __future__ import print_function
from builtins import input

def main():
    T = int(input())
    if T < 1 or T > 100:
        raise RuntimeError("T is not within the valid range")
    for i in range(T):
        N,P = map(int, input().split())
        R = map(int, input().split())
        pantry = []
        for j in range(N):
            pantry.append(sorted(map(int, input().split())))
        r = Ratatouille(pantry, R)
        print("Case #" + str(i + 1) + ": " + r)

def Ratatouille(pantry, R):
    r,i = 0,0
    while True:
        selected = [0] * len(R)
        Rmin = [ing * i * 0.9 for ing in R]
        Rmax = [ing * i * 1.1 for ing in R]
        for j in range(len(R)):
            if len(pantry[j]) == 0:
                return str(r)
            rem = []
            for k in range(len(pantry[j])):
                if pantry[j][k] < Rmin[j]:
                    rem.append(pantry[j][k])
                if pantry[j][k] > Rmax[j]:
                    break
                if Rmin[j] <= pantry[j][k] and Rmax[j] >= pantry[j][k]:
                    selected[j] = pantry[j][k]
                    break
            for k in range(len(rem)):
                pantry[j].remove(rem[k])
        if all(item != 0 for item in selected):
            for j in range(len(selected)):
                pantry[j].remove(selected[j])
            r += 1
        else:
            i += 1
    return str(r)

if __name__=="__main__":
    main()
