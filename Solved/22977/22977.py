# Problem No.: 22977
# Solver:      Jinmin Goh
# Date:        20220712
# URL: https://www.acmicpc.net/problem/22977

import sys

def main():
    n = int(sys.stdin.readline().rstrip())
    dots = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
    ans = 0
    for i in range(1, n):
        ans += abs(dots[i][0] - dots[i - 1][0]) + abs(dots[i][1] - dots[i - 1][1])
    print(ans - (dots[-1][0] - dots[0][0]))
    return

if __name__ == "__main__":
    main()