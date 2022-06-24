# Problem No.: 7579
# Solver:      Jinmin Goh
# Date:        20220624
# URL: https://www.acmicpc.net/problem/7579

import sys

def main():
    n, m = map(int, input().split())
    memory = list(map(int, sys.stdin.readline().split()))
    cost = list(map(int, sys.stdin.readline().split()))
    sum_val = sum(cost)
    dp_table = [[0 for _ in range(sum_val + 1)] for __ in range(n)]
    for i in range(n):
        for j in range(sum_val + 1):
            dp_table[i][j] = dp_table[i - 1][j]
            if j - cost[i] >= 0:
                dp_table[i][j] = max(dp_table[i][j], dp_table[i - 1][j - cost[i]] + memory[i])
    ans = 0
    while True:
        if dp_table[n - 1][ans] >= m:
            print(ans)
            break
        ans += 1
    return

if __name__ == "__main__":
    main()