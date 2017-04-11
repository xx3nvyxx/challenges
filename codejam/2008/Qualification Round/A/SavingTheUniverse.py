#!/user/bin/env python
"""Google Code Jam 2008: Problem A. Saving the Universe"""

from __future__ import print_function
from builtins import input

def main():
    N = int(input())
    if N < 1 or N > 20:
        raise RuntimeError("N is not within the valid range")
    for i in range(N):
        engines = set()
        queries = []
        S = int(input())
        for j in range(S):
            engines.add(input())
        Q = int(input())
        for j in range(Q):
            queries.append(input())
        r = SavingtheUniverse(engines, queries)
        print("Case #" + str(i + 1) + ": " + r)

def SavingtheUniverse(engines, queries):
    if len(engines.difference(queries)) > 0:
        return "0"
    r = 0
    usedEngines = set()
    for i in range(len(queries)):
        usedEngines.add(queries[i])
        if len(engines - usedEngines) == 0:
            r = r + 1
            usedEngines = set()
            usedEngines.add(queries[i])
    return str(r)


if __name__=="__main__":
    main()
