# Problem No.: 2098
# Solver:      Jinmin Goh
# Date:        20220624
# URL: https://www.acmicpc.net/problem/2098

import sys

def solve(cost, dp_table, curr, visited):
    n = len(cost)
    # if visited all cities
    if visited == ((1 << n) - 1):
        # can go back to 0
        if cost[curr][0] != 0:
            return cost[curr][0]
        # can't go back to 0
        else:
            return 10 ** 9
    # not visited all cities
    else:
        if dp_table[curr][visited] == -1:
            min_val = 10 ** 9
            for next in range(n):
                if not visited & (1 << next) and cost[curr][next] != 0:
                    min_val = min(min_val, solve(cost, dp_table, next, visited | (1 << next)) + cost[curr][next])
            dp_table[curr][visited] = min_val
        return dp_table[curr][visited]

def main():
    n = int(input())
    cost = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    dp_table = [[-1 for _ in range(1 << n)] for __ in range(n)]
    ans = solve(cost, dp_table, 0, 1)
    print(ans)
    return

if __name__ == "__main__":
    main()