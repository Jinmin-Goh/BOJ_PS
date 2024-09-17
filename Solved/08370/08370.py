# Problem No.: 8370
# Solver:      Jinmin Goh
# Date:        20220914
# URL: https://www.acmicpc.net/problem/8370

import sys

def main():
    a, b, c, d = map(int, sys.stdin.readline().split())
    print(a * b + c * d)
    return

if __name__ == "__main__":
    main()