# Problem No.: 18784
# Solver:      Jinmin Goh
# Date:        20200714
# URL: https://www.acmicpc.net/problem/18784

import sys

def main():
    n = int(input())
    coordinates = {}
    coordX = {}
    coordY = {}
    for _ in range(n):
        x, y = map(int, sys.stdin.readline().split())
        if x not in coordX:
            coordX[x] = [(x, y)]
        else:
            coordX[x].append((x, y))
        if y not in coordY:
            coordY[y] = [(x, y)]
        else:
            coordY[y].append((x, y))
        coordinates[(x, y)] = 0
    
    validX = []
    validY = []
    validDot = []

    for i in coordX:
        if len(coordX[i]) > 1:
            validX.append(i)
            for j in coordX[i]:
                coordinates[j] += 1
    for i in coordY:
        if len(coordY[i]) > 1:
            validY.append(i)
            for j in coordY[i]:
                coordinates[j] += 1
                if coordinates[j] == 2:
                    validDot.append(j)
    
    ans = 0
    
    if not validDot:
        print(0)
        return
    
    for dot in validDot:
        [x, y] = dot
        #print(x, y)
        xSum = 0
        ySum = 0
        for dotX in coordX[x]:
            xSum += abs(dot[1] - dotX[1])
        for dotY in coordY[y]:
            ySum += abs(dot[0] - dotY[0])
        ans += abs(xSum * ySum)
        
    print(ans)
    return

if __name__ == "__main__":
    main()