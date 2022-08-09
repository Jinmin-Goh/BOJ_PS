# Problem No.: 1271
# Solver:      Jinmin Goh
# Date:        20220809
# URL: https://www.acmicpc.net/problem/1271

import sys

def main():
    n, m = map(int, sys.stdin.readline().split())
    print(n // m)
    print(n % m)
    return

if __name__ == "__main__":
    main()