# Problem No.: 2738
# Solver:      Jinmin Goh
# Date:        20220724
# URL: https://www.acmicpc.net/problem/2738

import sys

def main():
    n, m = map(int, sys.stdin.readline().split())
    a = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    b = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    for i in range(n):
        for j in range(m):
            print(a[i][j] + b[i][j], end=" ")
        print()
    return

if __name__ == "__main__":
    main()