# Problem No.: 14489
# Solver:      Jinmin Goh
# Date:        20220916
# URL: https://www.acmicpc.net/problem/14489

import sys

def main():
    a, b = map(int, sys.stdin.readline().split())
    c = int(sys.stdin.readline().rstrip())
    print(a + b if (a + b) < 2 * c else (a + b) - 2 * c)
    return

if __name__ == "__main__":
    main()