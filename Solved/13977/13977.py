# Problem No.: 13977
# Solver:      Jinmin Goh
# Date:        20220707
# URL: https://www.acmicpc.net/problem/13977

import sys

def main():
    n = int(input())
    f = [1 for _ in range(4000001)]
    for i in range(1, 4000001):
        f[i] = (f[i - 1] * i) % 1000000007
    for _ in range(n):
        a, b = map(int, sys.stdin.readline().split())
        print((f[a] * pow(f[b], -1, 1000000007) * pow(f[a - b], -1, 1000000007)) % 1000000007)
    return

if __name__ == "__main__":
    main()