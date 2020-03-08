# Problem No.: 1149
# Solver:      Jinmin Goh
# Date:        20200308
# URL: https://www.acmicpc.net/problem/1149

import sys

def main():
    n = int(input())
    cost = []
    for i in range(n):
        temp = input().split()
        temp = [int(_) for _ in temp]
        cost.append(temp)
    costSum = [[None] * 3 for _ in range(n)] 
    costSum[0] = cost[0][:]
    for i in range(1, n):
        costSum[i][0] = cost[i][0] + min(costSum[i - 1][1], costSum[i - 1][2])
        costSum[i][1] = cost[i][1] + min(costSum[i - 1][0], costSum[i - 1][2])
        costSum[i][2] = cost[i][2] + min(costSum[i - 1][1], costSum[i - 1][0])
    print(min(costSum[-1]))

if __name__ == "__main__":
    main()