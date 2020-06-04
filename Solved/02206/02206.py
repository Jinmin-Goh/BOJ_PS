# Problem No.: 2206
# Solver:      Jinmin Goh
# Date:        20200604
# URL: https://www.acmicpc.net/problem/2206

import sys

def main():
    # parsing
    n, m = map(int, input().split())
    table = []
    for _ in range(n):
        temp = sys.stdin.readline().strip()
        table.append([i for i in temp])
    
    # distance table
    distance = [[[-1, -1] for _ in range(m)] for __ in range(n)]
    distance[0][0] = [1, 1]
    
    # BFS
    queue = [((0, 0), False)]
    while queue:
        temp = queue.pop(0)
        row = temp[0][0]
        col = temp[0][1]
        blockFlag = temp[1]
        if row > 0:
            if table[row - 1][col] == "0":
                if distance[row - 1][col][blockFlag] == -1:
                    distance[row - 1][col][blockFlag] = distance[row][col][blockFlag] + 1
                    queue.append(((row - 1, col), blockFlag))
            else:
                if not blockFlag:
                    distance[row - 1][col][1] = distance[row][col][0] + 1
                    queue.append(((row - 1, col), True))
        if row < n - 1:
            if table[row + 1][col] == "0":
                if distance[row + 1][col][blockFlag] == -1:
                    distance[row + 1][col][blockFlag] = distance[row][col][blockFlag] + 1
                    queue.append(((row + 1, col), blockFlag))
            else:
                if not blockFlag:
                    distance[row + 1][col][1] = distance[row][col][0] + 1
                    queue.append(((row + 1, col), True))
        if col > 0:
            if table[row][col - 1] == "0":
                if distance[row][col - 1][blockFlag] == -1:
                    distance[row][col - 1][blockFlag] = distance[row][col][blockFlag] + 1
                    queue.append(((row, col - 1), blockFlag))
            else:
                if not blockFlag:
                    distance[row][col - 1][1] = distance[row][col][0] + 1
                    queue.append(((row, col - 1), True))
        if col < m - 1:
            if table[row][col + 1] == "0":
                if distance[row][col + 1][blockFlag] == -1:
                    distance[row][col + 1][blockFlag] = distance[row][col][blockFlag] + 1
                    queue.append(((row, col + 1), blockFlag))
            else:
                if not blockFlag:
                    distance[row][col + 1][1] = distance[row][col][0] + 1
                    queue.append(((row, col + 1), True))
    
    # print phase
    if distance[n - 1][m - 1][0] == -1 and distance[n - 1][m - 1][1] == -1:
        print(-1)
    elif distance[n - 1][m - 1][0] == -1:
        print(distance[n - 1][m - 1][1])
    elif distance[n - 1][m - 1][1] == -1:
        print(distance[n - 1][m - 1][0])
    else:
        print(min(distance[n - 1][m - 1]))
    return

if __name__ == "__main__":
    main()