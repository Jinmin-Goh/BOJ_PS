# Problem No.: 10868
# Solver:      Jinmin Goh
# Date:        20220617
# URL: https://www.acmicpc.net/problem/10868

import sys

# RMQ (Range Minimum/Maximum Query)

def main():
    n, m = map(int, input().split())
    nums = [int(sys.stdin.readline()) for _ in range(n)]
    query = [tuple(map(int, sys.stdin.readline().split())) for _ in range(m)]
    dp_table = [[(10 ** 9 + 1) for _ in range(20)] for __ in range(n + 1)]

    for i in range(20):
        for j in range(1, n + 1):
            if i == 0:
                dp_table[j][i] = nums[j - 1]
                continue
            if j + 2 ** i - 1 > n:
                break
            dp_table[j][i] = min(dp_table[j][i - 1], dp_table[j + 2 ** (i - 1)][i - 1])

    for (p, q) in query:
        if p > q:
            p, q = q, p
        for i in range(20, -1, -1):
            if 2 ** i > q - p + 1:
                continue
            print(min(dp_table[p][i], dp_table[q - (2 ** i) + 1][i]))
            break
    return

if __name__ == "__main__":
    main()