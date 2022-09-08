# Problem No.: 18301
# Solver:      Jinmin Goh
# Date:        20220908
# URL: https://www.acmicpc.net/problem/18301

import sys

def main():
    a, b, c = map(int, sys.stdin.readline().split())
    print((a + 1) * (b + 1) // (c + 1) - 1)
    return

if __name__ == "__main__":
    main()