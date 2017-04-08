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
  openGroups = {N: 1}
  while K > 0:
    s = sorted(openGroups.keys(), reverse=True)[0]
    m = openGroups[s]
    del openGroups[s]
    s = s - 1
    r = [s//2+s%2, s//2]
    openGroups[r[0]] = openGroups.setdefault(r[0], 0) + m
    openGroups[r[1]] = openGroups.setdefault(r[1], 0) + m
    K = K - m
  return r


if __name__=="__main__":
    main()
