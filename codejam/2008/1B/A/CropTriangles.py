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
    trees = dict()
    trees[(X%3,Y%3)] = 1
    r = 0
    checked = set()
    for i in range(1,n):
        X = (A * X + B) % M
        Y = (C * Y + D) % M
        trees[(X%3,Y%3)] = trees.get((X%3,Y%3),0)+1
    for a in trees.keys():
        for b in trees.keys():
            for c in trees.keys():
                if frozenset({a,b,c}) in checked:
                    continue
                else:
                    checked.add(frozenset({a,b,c}))
                if (a[0]+b[0]+c[0]) % 3 == 0 and (a[1]+b[1]+c[1]) % 3 == 0:
                    if a == b and b == c:
                        t = trees[a]
                        r += (t*(t-1)*(t-2))/6
                    elif a == b:
                        t = trees[a]
                        r += trees[c] * (t*(t-1))/2
                    elif a == c:
                        t = trees[a]
                        r += trees[b] * (t*(t-1))/2
                    elif b == c:
                        t = trees[b]
                        r += trees[a] * (t*(t-1))/2
                    else:
                        r += trees[a]*trees[b]*trees[c]
    return str(r)

if __name__=="__main__":
    main()
