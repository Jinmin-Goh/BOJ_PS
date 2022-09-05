# Problem No.: 14652
# Solver:      Jinmin Goh
# Date:        20220905
# URL: https://www.acmicpc.net/problem/14652

import sys

def main():
    n, m, k = map(int, sys.stdin.readline().split())
    print(k // m, k % m)
    return

if __name__ == "__main__":
    main()