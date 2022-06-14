# Problem No.: 13172
# Solver:      Jinmin Goh
# Date:        20220614
# URL: https://www.acmicpc.net/problem/13172

import sys

P = 1000000007

def main():
    m = int(input())
    ans = 0
    for _ in range(m):
        ni, si = map(int, input().split())
        ans += si * pow(ni, -1, P)
        ans %= P
    print(ans)
    return

if __name__ == "__main__":
    main()