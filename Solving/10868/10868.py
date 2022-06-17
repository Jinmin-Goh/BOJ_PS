# Problem No.: 10868
# Solver:      Jinmin Goh
# Date:        20220617
# URL: https://www.acmicpc.net/problem/10868

import sys

# RMQ (Range Minimum/Maximum Query)

def solve(nums, dp_table, p, q):
    if p == q:
        dp_table[p][0] = nums[p - 1]
        return dp_table[p][0]
    else:
        for i in range(19, -1, -1):
            if 2 ** i >= q - p + 1:
                continue
            print(p, q, i)
            dp_table[p][i] = solve(nums, dp_table, p, p + (2 ** i) - 1) 
            dp_table[q - (2 ** i) + 1][i] = solve(nums, dp_table, q - (2 ** i) + 1, q)
            
            return min(dp_table[p][i], dp_table[q - (2 ** i) + 1][i])

def main():
    n, m = map(int, input().split())
    nums = [int(sys.stdin.readline()) for _ in range(n)]
    query = [tuple(map(int, sys.stdin.readline().split())) for _ in range(m)]
    dp_table = [[(10 ** 9 + 1) for _ in range(20)] for __ in range(n + 1)]
    solve(nums, dp_table, 1, n)
    #print(dp_table)
    for (p, q) in query:
        if p > q:
            p, q = q, p
        for i in range(20, 0, -1):
            if 2 ** i >= q - p + 1:
                continue
            print(p, q, i, q - (2 ** i) + 1)
            print(min(dp_table[p][i], dp_table[q - (2 ** i) + 1][i]))
            break
    return

if __name__ == "__main__":
    main()