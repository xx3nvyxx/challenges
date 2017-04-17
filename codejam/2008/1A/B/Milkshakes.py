#!/user/bin/env python
"""Google Code Jam 2008: Problem B. Milkshakes"""

from __future__ import print_function
from builtins import input

def main():
    C = int(input())
    for i in range(C):
        N = int(input())
        M = int(input())
        customers = dict()
        for j in range(M):
            p = map(int, input().split())
            customers[j] = []
            for k in range(1, len(p), 2):
                customers[j].append((p[k]-1,p[k+1]))
        r = Milkshakes(N,customers)
        print("Case #" + str(i + 1) + ": " + r)

def Milkshakes(N,customers):
    r = [None]*(N)
    while len(customers) > 0:
        k = sorted(customers, key=lambda x:len(customers[x]))
        curCust =  customers[k[0]]
        if len(curCust) == 0:
            return "IMPOSSIBLE"
        elif len(curCust) == 1: #simple case, if a customer only likes one flavor
            flavor = curCust[0][0]
            malted = curCust[0][1]
            if r[flavor] == None:
                r[flavor] = malted
                for key in customers.keys():
                    if (flavor,malted) in customers[key]:
                        del customers[key]
                    elif (flavor, 1-malted) in customers[key]:
                        customers[key].remove((flavor, 1-malted))
            elif r[flavor] != malted:
                return "IMPOSSIBLE" #this will probably never trigger since we delete opposing malts above
            else:
                del customers[k[0]]
                continue
        else:
            prefs = {}
            for key in customers:
                curcust = customers[key]
                for i in range(len(curCust)):
                    prefs[curCust[i]] = prefs.get(curCust[i], 0) + 1
            k = sorted(prefs, key=lambda x:prefs[x], reverse=True)
            flavor = k[0][0]
            malted = k[0][1]
            if r[flavor] == None:
                r[flavor] = malted
                for key in customers.keys():
                    if (flavor,malted) in customers[key]:
                        del customers[key]
                    elif (flavor, 1-malted) in customers[key]:
                        customers[key].remove((flavor, 1-malted))
            elif r[flavor] != malted:
                return "IMPOSSIBLE" #this will probably never trigger since we delete opposing malts above
            else:
                del customers[k[0]]
                continue
    return " ".join( ["0" if v is None else str(v) for v in r] )

if __name__=="__main__":
    main()
