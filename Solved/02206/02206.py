# Problem No.: 2206
# Solver:      Jinmin Goh
# Date:        20220613
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
    distance[0][0] = [1, -1]
    
    # BFS
    queue = [((0, 0), 0)]
    while queue:
        temp = []
        for node in queue:
            row = node[0][0]
            col = node[0][1]
            blockFlag = node[1]
            if row > 0:
                if table[row - 1][col] == "0":  # path
                    if distance[row - 1][col][blockFlag] == -1:
                        distance[row - 1][col][blockFlag] = distance[row][col][blockFlag] + 1
                        temp.append(((row - 1, col), blockFlag))
                else:   # wall
                    if not blockFlag:   # not broke the wall yet
                        if distance[row - 1][col][1] == -1:     # not visited yet
                            distance[row - 1][col][1] = distance[row][col][blockFlag] + 1
                            temp.append(((row - 1, col), 1))
            if row < n - 1:
                if table[row + 1][col] == "0":  # path
                    if distance[row + 1][col][blockFlag] == -1:
                        distance[row + 1][col][blockFlag] = distance[row][col][blockFlag] + 1
                        temp.append(((row + 1, col), blockFlag))
                else:   # wall
                    if not blockFlag:   # not broke the wall yet
                        if distance[row + 1][col][1] == -1:     # not visited yet
                            distance[row + 1][col][1] = distance[row][col][blockFlag] + 1
                            temp.append(((row + 1, col), 1))
            if col > 0:
                if table[row][col - 1] == "0":  # path
                    if distance[row][col - 1][blockFlag] == -1:
                        distance[row][col - 1][blockFlag] = distance[row][col][blockFlag] + 1
                        temp.append(((row, col - 1), blockFlag))
                else:   # wall
                    if not blockFlag:   # not broke the wall yet
                        if distance[row][col - 1][1] == -1:     # not visited yet
                            distance[row][col - 1][1] = distance[row][col][blockFlag] + 1
                            temp.append(((row, col - 1), 1))
            if col < m - 1:
                if table[row][col + 1] == "0":  # path
                    if distance[row][col + 1][blockFlag] == -1:
                        distance[row][col + 1][blockFlag] = distance[row][col][blockFlag] + 1
                        temp.append(((row, col + 1), blockFlag))
                else:   # wall
                    if not blockFlag:   # not broke the wall yet
                        if distance[row][col + 1][1] == -1:     # not visited yet
                            distance[row][col + 1][1] = distance[row][col][blockFlag] + 1
                            temp.append(((row, col + 1), 1))
        queue = temp
    
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