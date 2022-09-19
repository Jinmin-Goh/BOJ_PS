# Problem No.: 25625
# Solver:      Jinmin Goh
# Date:        20220919
# URL: https://www.acmicpc.net/problem/25625

import sys

def main():
    x, y = map(int, sys.stdin.readline().split())
    if x > y:
        print(x + y)
    else:
        print(y - x)
    return

if __name__ == "__main__":
    main()