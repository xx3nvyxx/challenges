#!/usr/bin/env python
"""Google Code Jam 2008: Problem A. Alien Numbers"""

from builtins import input

def main():
    T = int(input())
    if T < 1 or T > 100:
        raise RuntimeError("T is not within the valid range")
    for i in range(T):
         alien_number,source_language,target_language = input().split()
         r = translate(alien_number, source_language, target_language)
         print("Case #" + str(i + 1) + ": " + r)
        
def translate(A, S, T):
    i = sourceToInt(A, S)
    return intToTarget(i, T)

def sourceToInt(A, S):
    base = len(S)
    l = list()
    for c in A:
        l.append(S.index(c))
    r = 0
    for i,n in enumerate(reversed(l)):
        r = r + ((base ** i) * n)
    return r

def intToTarget(A, T):
    base = len(T)
    l = list()
    while A != 0:
        l.append(A % base)
        A = A // base
    r = ""
    for i in l:
        r = T[i] + r
    return r

if __name__=="__main__":
    main()
