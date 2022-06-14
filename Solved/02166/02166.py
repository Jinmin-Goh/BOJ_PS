# Problem No.: 2166
# Solver:      Jinmin Goh
# Date:        20220614
# URL: https://www.acmicpc.net/problem/2166

import sys

def main():
    n = int(input())
    poly = []
    for _ in range(n):
        x, y = map(int, input().split())
        poly.append((x, y))
    base = poly[0]
    ans = 0.0
    for i in range(1, n - 1):
        p = poly[i]
        q = poly[i + 1]
        ans += ((p[0] - base[0]) * (q[1] - base[1]) - (p[1] - base[1]) * (q[0] - base[0])) * 0.5
    ans = abs(ans)
    print(f"{ans:.1f}")
    return

if __name__ == "__main__":
    main()