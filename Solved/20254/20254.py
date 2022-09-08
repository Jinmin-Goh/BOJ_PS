# Problem No.: 20254
# Solver:      Jinmin Goh
# Date:        20220908
# URL: https://www.acmicpc.net/problem/20254

import sys

def main():
    a, b, c, d = map(int, sys.stdin.readline().split())
    print(56 * a + 24 * b + 14 * c + 6 * d)
    return

if __name__ == "__main__":
    main()