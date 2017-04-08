#!/user/bin/env python
"""Google Code Jam 2017: Problem A. Oversized Pancake Flipper"""

from __future__ import print_function
from builtins import input

def main():
    T = int(input())
    if T < 1 or T > 100:
        raise RuntimeError("T is not within the valid range")
    for i in range(T):
        S,K = map(lambda x,y:x(y), (str,int), input().split())
        r = OversizedPancakeFlipper(list(S),K)
        print("Case #" + str(i + 1) + ": " + r)

def OversizedPancakeFlipper(S,K):
    r = 0
    for i in range(len(S)):
        if S[i] == '-':
            for j in range(K):
                try:
                    if S[i+j] == '-':
                        S[i+j] = '+'
                    else:
                        S[i+j] = '-'
                except IndexError:
                   return "IMPOSSIBLE"
            r += 1
    return str(r)

if __name__=="__main__":
    main()
