#!/user/bin/env python
"""Google Code Jam 2008: Problem A. Crop Triangles"""

from __future__ import print_function
from builtins import input

def main():
    N = int(input())
    if N < 1 or N > 10:
        raise RuntimeError("N is not within the valid range")
    for i in range(N):
        n,A,B,C,D,X,Y,M = map(int, input().split())
        r = CropTriangles(n,A,B,C,D,X,Y,M)
        print("Case #" + str(i + 1) + ": " + r)

def CropTriangles(n,A,B,C,D,X,Y,M):
    trees = set()
    trees.add((X,Y))
    r = set()
    checked = set()
    for i in range(1,n):
        X = (A * X + B) % M
        Y = (C * Y + D) % M
        trees.add((X,Y))
    for a in trees:
        checked.add(a)
        for b in trees-checked:
            if a == b:
                continue
            for c in trees-checked:
                if a == c or b == c:
                    continue
                if (a[0]+b[0]+c[0]) % 3 == 0 and (a[1]+b[1]+c[1]) % 3 == 0:
                    r.add(frozenset({a,b,c}))
    return str(len(r))

if __name__=="__main__":
    main()
