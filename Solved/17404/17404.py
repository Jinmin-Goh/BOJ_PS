# Problem No.: 17404
# Solver:      Jinmin Goh
# Date:        20220616
# URL: https://www.acmicpc.net/problem/17404

import sys

def main():
    n = int(input())
    cost = []
    for _ in range(n):
        a, b, c = map(int, input().split())
        cost.append((a, b, c))
    ans = 10 ** 7
    for p in range(3):
        costSum = [[None, None, None] for _ in range(n)]
        costSum[0] = [10 ** 7, 10 ** 7, 10 ** 7]
        costSum[0][p] = cost[0][p]
        for i in range(1, n):
            costSum[i][0] = cost[i][0] + min(costSum[i - 1][1], costSum[i - 1][2])
            costSum[i][1] = cost[i][1] + min(costSum[i - 1][0], costSum[i - 1][2])
            costSum[i][2] = cost[i][2] + min(costSum[i - 1][1], costSum[i - 1][0])
        for i in range(3):
            if i == p:
                continue
            ans = min(ans, costSum[n - 1][i])
    print(ans)
    return

if __name__ == "__main__":
    main()