# Problem No.: 17371
# Solver:      Jinmin Goh
# Date:        20220708
# URL: https://www.acmicpc.net/problem/17371

import sys

def dist(a, b):
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5

def main():
    n = int(input())
    dots = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
    ans = None
    min_val = 10 ** 5
    for i in range(n):
        max_val = 0
        for j in range(n):
            if i == j:
                continue
            val = dist(dots[i], dots[j])
            if max_val < val:
                max_val = val
        if min_val > max_val:
            ans = dots[i]
            min_val = max_val
    print(ans[0], ans[1])
    return

if __name__ == "__main__":
    main()