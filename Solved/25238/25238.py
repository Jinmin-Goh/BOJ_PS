# Problem No.: 25238
# Solver:      Jinmin Goh
# Date:        20220820
# URL: https://www.acmicpc.net/problem/25238

import sys

def main():
    a, b = map(int, sys.stdin.readline().split())
    print(0 if 10000 <= a * (100 - b) else 1)
    return

if __name__ == "__main__":
    main()