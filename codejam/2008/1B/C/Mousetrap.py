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
    a = range(1,K+1)
    c = 1
    order = dict()
    while not (set(d) <= set(order.keys())):
        order[a.pop(0)] = c
        if len(order) == K:
            break
        offset = c % len(a)
        c += 1
        a = a[offset:]+a[:offset]
        #print(a)
    r = []
    for i in range(len(d)):
        r.append(str(order[d[i]]))
    return " ".join(r)

if __name__=="__main__":
    main()
