# Problem No.: 16917
# Solver:      Jinmin Goh
# Date:        20220702
# URL: https://www.acmicpc.net/problem/16917

import sys

def main():
    a, b, c, x, y = map(int, input().split())
    ans = 0
    if a + b > 2 * c:
        ans += min(x, y) * 2 * c
    else:
        ans += (a + b) * min(x, y)
    if x > y:
        if a > 2 * c:
            ans += (x - y) * 2 * c
        else:
            ans += (x - y) * a
    else:
        if b > 2 * c:
            ans += (y - x) * 2 * c
        else:
            ans += (y - x) * b
    print(ans)
    return

if __name__ == "__main__":
    main()