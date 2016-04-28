#!/user/bin/env python
"""Google Code Jam 2008: Problem B. Always Turn Left"""

from __future__ import print_function
from builtins import input
from operator import itemgetter

def main():
    N = int(input())
    if N < 1 or N > 100:
        raise RuntimeError("N is not within the valid range")
    for i in range(N):
        entrance_to_exit,exit_to_entrance = input().split()
        print("Case #" + str(i + 1) + ":")
        AlwaysTurnLeft(entrance_to_exit,exit_to_entrance)

def AlwaysTurnLeft(entrance_to_exit,exit_to_entrance):
    maze = {}
    x,y,angle = 0,0,270
    x,y,angle = followMaze(maze, x, y, angle, entrance_to_exit)
    angle = (angle + 180) % 360
    exit = (x,y)
    followMaze(maze, x, y, angle, exit_to_entrance)
    del maze[(0,0)]
    del maze[exit]
    rooms = maze.keys()
    for r in range(max(rooms, key=itemgetter(1))[1], min(rooms, key=itemgetter(1))[1] - 1, -1):
        for c in range(min(rooms, key=itemgetter(0))[0], max(rooms, key=itemgetter(0))[0] + 1):
            print("%x" % maze[(c,r)], end="")
        print()



def followMaze(maze, x, y, angle, steps):
    for step in steps:
        if step == "W":
            if angle == 0:
                maze[x,y] = maze.get((x,y), 0) | 8
                x += 1
                maze[x,y] = maze.get((x,y), 0) | 4
            if angle == 90:
                maze[x,y] = maze.get((x,y), 0) | 1
                y += 1
                maze[x,y] = maze.get((x,y), 0) | 2
            if angle == 180:
                maze[x,y] = maze.get((x,y), 0) | 4
                x -= 1
                maze[x,y] = maze.get((x,y), 0) | 8
            if angle == 270:
                maze[x,y] = maze.get((x,y), 0) | 2
                y -= 1
                maze[x,y] = maze.get((x,y), 0) | 1
        if step == "L":
            angle = (angle + 90) % 360
        if step == "R":
            angle = (angle + 270) % 360
    return (x,y, angle)


            


if __name__=="__main__":
    main()
