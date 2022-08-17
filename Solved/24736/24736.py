# Problem No.: 24736
# Solver:      Jinmin Goh
# Date:        20220817
# URL: https://www.acmicpc.net/problem/24736

import sys

def main():
    for _ in range(2):
        t, f, s, p, c = map(int, sys.stdin.readline().split())
        print(t * 6 + f * 3 + s * 2 + p + c * 2, end=' ')
    return

if __name__ == "__main__":
    main()