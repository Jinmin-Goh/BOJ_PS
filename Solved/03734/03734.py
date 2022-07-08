# Problem No.: 3734
# Solver:      Jinmin Goh
# Date:        20220708
# URL: https://www.acmicpc.net/problem/3734

import sys, math

def main():
    n, k = map(int, sys.stdin.readline().split())
    for t in range(10 ** 5):
        val = math.isqrt(t ** 2 + 4 * k * n)
        if (val ** 2) != (t ** 2 + 4 * k * n):
            continue
        if (val - t) % (2 * k) == 0:
            p = (val - t) // (2 * k)
            if p != 1:
                print(min(p, n // p), '*', max(p, n // p))
                break
        if (val + t) % (2 * k) == 0:
            p = (val + t) // (2 * k)
            if p != 1:
                print(min(p, n // p), '*', max(p, n // p))
                break

    return

if __name__ == "__main__":
    main()