#!/user/bin/env python
"""Google Code Jam 2008: Problem B. Train Timetable"""

from __future__ import print_function
from builtins import input

def main():
    N = int(input())
    if N < 1 or N > 100:
        raise RuntimeError("N is not within the valid range")
    for i in range(N):
        T = int(input())
        NA,NB = map(int, input().split())
        AB = []
        BA = []
        for j in range(NA):
            times = input().split()
            Dh,Dm = map(int, times[0].split(':'))
            Ah,Am = map(int, times[1].split(':'))
            Ah = Ah + ((Am + T) // 60)
            Am = (Am + T) % 60
            AB.append(((Dh,Dm),(Ah,Am)))
        for j in range(NB):
            times = input().split()
            Dh,Dm = map(int, times[0].split(':'))
            Ah,Am = map(int, times[1].split(':'))
            Ah = Ah + ((Am + T) // 60)
            Am = (Am + T) % 60
            BA.append(((Dh,Dm),(Ah,Am)))
        r = TrainTimetable(AB, BA)
        print("Case #" + str(i + 1) + ": " + r)

def TrainTimetable(AB, BA):
    A = 0
    minA = 0
    B = 0
    minB = 0
    for h in range(24):
        for m in range(60):
            dA = len([t for t in AB if t[0] == (h,m)])
            aA = len([t for t in BA if t[1] == (h,m)])
            A = A - dA + aA
            dB = len([t for t in BA if t[0] == (h,m)])
            aB = len([t for t in AB if t[1] == (h,m)])
            B = B - dB + aB
            minA = min(minA, A)
            minB = min(minB, B)
    return str(abs(minA)) + " " + str(abs(minB))

if __name__=="__main__":
    main()
