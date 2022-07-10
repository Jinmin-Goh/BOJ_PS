# Problem No.: 5361
# Solver:      Jinmin Goh
# Date:        20220710
# URL: https://www.acmicpc.net/problem/5361

import sys

def main():
    t = int(input())
    for _ in range(t):
        a, b, c, d, e = map(int, sys.stdin.readline().split())
        print(f'${a * 350.34 + b * 230.90 + c * 190.55 + d * 125.30 + e * 180.90:.2f}')
    return

if __name__ == "__main__":
    main()