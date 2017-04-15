#!/user/bin/env python
"""Google Code Jam 2017: Problem C. Play the Dragon"""

from __future__ import print_function
from builtins import input

def main():
    T = int(input())
    if T < 1 or T > 100:
        raise RuntimeError("T is not within the valid range")
    for i in range(T):
        Hd,Ad,Hk,Ak,B,D = map(int, input().split())
        r = PlaytheDragon(Hd,Ad,Hk,Ak,B,D)
        print("Case #" + str(i + 1) + ": " + r)

def PlaytheDragon(Hd,Ad,Hk,Ak,B,D):
    H = Hd
    queue = []
    state = [0,Hd,Ad,Hk,Ak]
    queue.append(state)
    seen = set()
    while len(queue) > 0:
        turn,Hd,Ad,Hk,Ak = queue.pop(0)
        tag = str(Hd) + " " + str(Ad) + " " + str(Hk) + " " + str(Ak)
        if tag in seen:
            continue
        else:
            seen.add(tag)
        turn += 1
        if Ad >= Hk:
            return str(turn)
        if Ak < Hd:
            attack = (turn,Hd-Ak,Ad,Hk-Ad,Ak)
            queue.append(attack)
            buff   = (turn,Hd-Ak,Ad+B,Hk,Ak)
            queue.append(buff)
            debuff = (turn,Hd-(Ak-D),Ad,Hk,max(Ak-D,0))
            queue.append(debuff)
        if Ak < H:
            heal = (turn,H-Ak,Ad,Hk,Ak)
            queue.append(heal)
    return "IMPOSSIBLE"

if __name__=="__main__":
    main()
