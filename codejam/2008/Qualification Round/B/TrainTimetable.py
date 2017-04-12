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
        keyTimes = set()
        AB = []
        BA = []
        for j in range(NA+NB):
            times = input().split()
            Dh,Dm = map(int, times[0].split(':'))
            Ah,Am = map(int, times[1].split(':'))
            Ah = Ah + ((Am + T) // 60)
            Am = (Am + T) % 60
            keyTimes.add((Dh,Dm))
            keyTimes.add((Ah,Am))
            if j < NA:
                AB.append(((Dh,Dm),(Ah,Am)))
            else:
                BA.append(((Dh,Dm),(Ah,Am)))
        r = TrainTimetable(keyTimes,AB, BA)
        print("Case #" + str(i + 1) + ": " + r)

def TrainTimetable(times, AB, BA):
    A = 0
    minA = 0
    B = 0
    minB = 0
    for time in sorted(times):
        h,m = time
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
