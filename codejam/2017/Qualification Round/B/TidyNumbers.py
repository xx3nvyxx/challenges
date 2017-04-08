#!/user/bin/env python
"""Google Code Jam 2017: Problem B. Tidy Numbers"""

from __future__ import print_function
from builtins import input

def main():
    T = int(input())
    if T < 1 or T > 100:
        raise RuntimeError("T is not within the valid range")
    for i in range(T):
        N = int(input())
        r = TidyNumbers(N)
        print("Case #" + str(i + 1) + ": " + r)

def TidyNumbers(N):
  for i in xrange(N, -1, -1):
    tidy = True
    s = str(i)
    for j in range(1, len(s)):
      if int(s[j]) < int(s[j-1]):
        tidy = False
        break
    if tidy:
      return s

if __name__=="__main__":
    main()
