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
  tiles = list()
  for i in range(K):
    tiles.append(addComplexity(2**i, 2**i, K, 1, C))
  return cleanTiles(tiles, S, K)

def addComplexity(current, original, K, curCplx, C):
  curString = format(current, "0"+str(K**curCplx)+"b")
  if curCplx == C:
    return curString
  r = 0
  for i in curString:
    r <<= K
    if i == "1":
      r |= 2**K-1
    else:
      r |= original
  return  addComplexity(r, original, K, curCplx+1, C)

def cleanTiles(tiles, S, K):
  r = list()
  while S != 0:
    i = bestTile(tiles, K)
    tiles = [x for x in tiles if x[i] != "1"]
    r.append(str(i+1))
    if len(tiles) == 0:
      return " ".join(r)
    S -= 1
  return "IMPOSSIBLE"

def bestTile(tiles, K):
  for i in range(len(tiles[0]):
    
    for r in tiles:
      b = int(r[i])
  g = [sum([int(r[i]) for r in tiles]) for i in range(0,len(tiles[0]))]
  print(g)
  return g.index(max(g))

if __name__=="__main__":
  main()
