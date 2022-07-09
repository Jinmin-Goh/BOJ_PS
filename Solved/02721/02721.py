# Problem No.: 2721
# Solver:      Jinmin Goh
# Date:        20220709
# URL: https://www.acmicpc.net/problem/2721

import sys

def main():
    t = int(input())
    for _ in range(t):
        n = int(sys.stdin.readline())
        # k * (k + 1) * (k + 2) // 2
        print((n * n * (n + 1) * (n + 1) // 4 + 3 * n * (n + 1) * (2 * n + 1) // 6 + n * (n + 1)) // 2)
    return

if __name__ == "__main__":
    main()