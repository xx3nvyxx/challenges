#!/user/bin/env python
"""Google Code Jam 2017: Problem A. Steed 2 Cruise Control"""

from __future__ import print_function
from builtins import input
import decimal

def main():
    T = int(input())
    if T < 1 or T > 100:
        raise RuntimeError("T is not within the valid range")
    for i in range(T):
        D,N = map(int, input().split())
        H = []
        for j in range(N):
            H.append(map(int, input().split()))
        r = Steed2CruiseControl(D,H)
        print("Case #" + str(i + 1) + ": " + r)

def Steed2CruiseControl(D,H):
    H.sort(key=lambda x: x[0], reverse=True)
    #print((D,H))
    end = (D,0)
    t = 0
    for i in range(len(H)):
        x = decimal.Decimal(end[0] - H[i][0]) / decimal.Decimal(H[i][1] - end[1])
        #print(x)
        t = max(t,x)
    return '{:.6f}'.format(D/t)

if __name__=="__main__":
    main()
