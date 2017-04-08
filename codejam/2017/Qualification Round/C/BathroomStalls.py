#!/user/bin/env python
"""Google Code Jam 2017: Problem C. Bathroom Stalls"""

from __future__ import print_function
from builtins import input

def main():
    T = int(input())
    if T < 1 or T > 100:
        raise RuntimeError("T is not within the valid range")
    for i in range(T):
        N,K = map(int, input().split())
        r = BathroomStalls(N,K)
        print("Case #" + str(i + 1) + ": " + str(r[0]) + " " + str(r[1]))

def BathroomStalls(N,K):
    openGroups = [N]
    for i in range(K):
      openGroups.sort()
      s = openGroups.pop() - 1
      r = [s//2+s%2, s//2]
      openGroups.extend(r)
    return r


if __name__=="__main__":
    main()
