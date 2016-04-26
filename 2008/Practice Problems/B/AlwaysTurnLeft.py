#!/user/bin/env python
"""Google Code Jam 2008: Problem B. Always Turn Left"""

from builtins import input

def main():
N = int(input())
if N < 1 or N > 100:
    raise RuntimeError("N is not within the valid range")
for i in range(N):
    entrance_to_exit,exit_to_entrance = input().split()
    r = AlwaysTurnLeft(entrance_to_exit,exit_to_entrance)
    print("Case #" + str(i + 1) + ": " + r)

def AlwaysTurnLeft(entrance_to_exit,exit_to_entrance):
    pass

if __name__=="__main__"
    main()
