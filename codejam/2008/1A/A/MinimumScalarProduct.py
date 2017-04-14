#!/user/bin/env python
"""Google Code Jam 2008: Problem A. Minimum Scalar Product"""

from __future__ import print_function
from builtins import input

def main():
    T = int(input())
    for i in range(T):
        n = int(input())
        x = map(int, input().split())
        y = map(int, input().split())
        r = MinimumScalarProduct(x,y)
        print("Case #" + str(i + 1) + ": " + r)

def MinimumScalarProduct(x,y):
    x.sort()
    y.sort(reverse=True)
    r = 0
    for i in range(len(x)):
        r += x[i] * y[i]
    return str(r)

if __name__=="__main__":
    main()
