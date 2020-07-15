# Problem No.: 18784
# Solver:      Jinmin Goh
# Date:        20200714
# URL: https://www.acmicpc.net/problem/18784

import sys

# solution reference: http://www.usaco.org/current/data/sol_triangles_silver_feb20.html

def main():
    modVal = 10 ** 9 + 7
    # parsing
    n = int(input())
    coordX = [[] for _ in range(2 * (10 ** 4) + 1)]
    coordY = [[] for _ in range(2 * (10 ** 4) + 1)]
    coordList = []

    for _ in range(n):
        x, y = map(int, sys.stdin.readline().split())
        # move dots parallel to [0, 2 * 10 ** 4]
        x += 10 ** 4
        y += 10 ** 4
        coordX[x].append(y)
        coordY[y].append(x)
        coordList.append((x, y))
    
    for i in range(2 * (10 ** 4) + 1):
        coordX[i].sort()
        coordY[i].sort()
    
    absSumValX = [[] for _ in range(20001)]
    absSumValY = [[] for _ in range(20001)]
    
    for i in range(2 * (10 ** 4) + 1):
        if len(coordX[i]) > 1:
            absSumValX[i] = {}
            tempSum = sum(coordX[i]) - len(coordX[i]) * coordX[i][0]
            absSumValX[i][coordX[i][0]] = tempSum
            for j in range(len(coordX[i]) - 1):
                # s_(i + 1) = s_i + (2 * i - n) * (x_(i + 1) - x_i)
                tempSum = tempSum + (2 * (j + 1) - len(coordX[i])) * (coordX[i][j + 1] - coordX[i][j])
                absSumValX[i][coordX[i][j + 1]] = tempSum

        if len(coordY[i]) > 1:
            absSumValY[i] = {}
            tempSum = sum(coordY[i]) - len(coordY[i]) * coordY[i][0]
            absSumValY[i][coordY[i][0]] = tempSum
            for j in range(len(coordY[i]) - 1):
                tempSum = tempSum + (2 * (j + 1) - len(coordY[i])) * (coordY[i][j + 1] - coordY[i][j])
                absSumValY[i][coordY[i][j + 1]] = tempSum
    
    ans = 0
    
    for node in coordList:
        (x, y) = node
        if not(absSumValX[x] and absSumValY[y]):
            continue
        ans += abs(absSumValX[x][y] * absSumValY[y][x]) % modVal
        ans %= modVal
        
    print(ans)
    return

if __name__ == "__main__":
    main()