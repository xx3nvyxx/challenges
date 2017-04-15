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
    state = (0,Hd,Ad,Hk,Ak,())
    queue.append(state)
    seen = dict()
    while len(queue) > 0:
        turn,Hd,Ad,Hk,Ak,pTag = queue.pop(0)
        tag = (Hd,Ad,Hk,Ak)
        if tag in seen:
            continue
        else:
            seen[tag] = pTag
        turn += 1
        if Ad >= Hk:
            while tag != ():
                #print(tag)
                tag = seen[tag]
            return str(turn)
        if Ak < Hd:
            attack = (turn,Hd-Ak,Ad,Hk-Ad,Ak,tag)
            queue.append(attack)
            buff   = (turn,Hd-Ak,Ad+B,Hk,Ak,tag)
            queue.append(buff)
        if (Ak-D) < Hd:
            debuff = (turn,Hd-max(Ak-D,0),Ad,Hk,max(Ak-D,0),tag)
            queue.append(debuff)
        if Ak < H:
            heal = (turn,H-Ak,Ad,Hk,Ak,tag)
            queue.append(heal)
    return "IMPOSSIBLE"

if __name__=="__main__":
    main()
