#!/user/bin/env python
"""Google Code Jam 2008: Problem C. Mousetrap"""

from __future__ import print_function
from builtins import input

def main():
    T = int(input())
    for i in range(T):
        K = int(input())
        d = map(int, input().split())[1:]
        r = Mousetrap(K, d)
        print("Case #" + str(i + 1) + ": " + r)

def Mousetrap(K, d):
    found = set()
    i = 0
    c = 1
    n = 1
    order = dict()
    while not (set(d) <= found):
        i = (i % K) + 1
        #print( i, c, n, r, d, found)
        if i in found:
            continue
        if n == c:
            found.add(i)
            order[i] = c
            c += 1
            n = 0
        n += 1
    r = []
    for i in range(len(d)):
        r.append(str(order[d[i]]))
    return " ".join(r)

if __name__=="__main__":
    main()
