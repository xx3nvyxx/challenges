#!/usr/bin/env python
"""Google Code Jam 2016: Problem D. Fractiles"""

from builtins import input

def main():
  T = int(input())
  if T < 1 or T > 100:
    raise RuntimeError("T is not within the valid range")
  for i in range(T):
     K,C,S = map(int, input().split())
     if K < 1 or K > 100:
       raise RuntimeError("K is not within the valid range")
     if C < 1 or C > 100:
       raise RuntimeError("C is not within the valid range")
     if S > K:
       raise RuntimeError("S is not within the valid range")
     r = pickTiles(K, C, S)
     print("Case #" + str(i + 1) + ": " + r)
    
def pickTiles(K, C, S):
  if S < ( (K+1) // 2 ) or ( C == 1 and S < K ):
    return "IMPOSSIBLE"
  if C == 1:
    return ' '.join(map(str,range(1, K+1)))
  #sequence = iK^(C-1) + (K-i)
  ret = list()
  for i in range( (K+1) // 2 ):
    ret.append( i * (K ** (C-1)) + (K - i))
  return ' '.join(map(str, ret))

if __name__=="__main__":
  main()
