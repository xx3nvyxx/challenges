#!/user/bin/env python
"""Google Code Jam 2016: Problem B. CloseMatch"""

from builtins import input

def main():
    T = int(input())
    if T < 1 or T > 200:
        raise RuntimeError("T is not within the valid range")
    for i in range(T):
        C,J = input().split()
        r = CloseMatch(C,J)
        print("Case #" + str(i + 1) + ": " + r)

def CloseMatch(C,J):
    rC = ['0']*len(C)
    rJ = ['0']*len(C)
    for i in range(len(C)):
        if  int(''.join(rC)) == int(''.join(rJ)):
            if C[i] == '?' and J[i] != '?':
                rC[i] = J[i]
                rJ[i] = J[i]
            elif C[i] != '?' and J[i] == '?':
                rC[i] = C[i]
                rJ[i] = C[i]
            elif C[i] == '?' and J[i] == '?':
                rC[i] = '0'
                rJ[i] = '0'
            else:
                rC[i] = C[i]
                rJ[i] = J[i]
        elif  int(''.join(rC)) > int(''.join(rJ)):
            if C[i] == '?' and J[i] != '?':
                rC[i] = '0'
                rJ[i] = J[i]
            elif C[i] != '?' and J[i] == '?':
                rC[i] = C[i]
                rJ[i] = '9'
            elif C[i] == '?' and J[i] == '?':
                rC[i] = '0'
                rJ[i] = '9'
            else:
                rC[i] = C[i]
                rJ[i] = J[i]
        else:
            if C[i] == '?' and J[i] != '?':
                rC[i] = '9'
                rJ[i] = J[i]
            elif C[i] != '?' and J[i] == '?':
                rC[i] = C[i]
                rJ[i] = '0'
            elif C[i] == '?' and J[i] == '?':
                rC[i] = '9'
                rJ[i] = '0'
            else:
                rC[i] = C[i]
                rJ[i] = J[i]
    return ''.join(rC) + ' ' + ''.join(rJ)
                


if __name__=="__main__":
    main()
