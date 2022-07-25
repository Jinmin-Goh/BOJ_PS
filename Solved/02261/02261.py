# Problem No.: 2261
# Solver:      Jinmin Goh
# Date:        20220725
# URL: https://www.acmicpc.net/problem/2261

import sys
from collections import deque

def dist(a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2

def brute_force(dots, s, e):
    val = 10 ** 9
    for i in range(s, e):
        for j in range(i + 1, e + 1):
            val = min(val, dist(dots[i], dots[j]))
    return val

def solve(dots, s, e):
    cnt = 1
    val = 10 ** 9
    if e - s < 3:
        return brute_force(dots, s, e)
    m = (s + e) // 2
    left_val = solve(dots, s, m - 1)
    right_val = solve(dots, m + 1, e)
    mid_val = solve2(dots, m, s, e, min(left_val, right_val))
    return min(left_val, right_val, mid_val)

def solve2(dots, m, s, e, min_val):
    temp = min_val
    left_cnt = 0
    right_cnt = 0
    while m - left_cnt >= s and min_val > (dots[m][0] - dots[m - left_cnt - 1][0]) ** 2:
        left_cnt += 1
    while m + right_cnt + 1 <= e and min_val > (dots[m][0] - dots[m + right_cnt + 1][0]) ** 2:
        right_cnt += 1
    x_candidate = dots[m - left_cnt: m + right_cnt + 1]
    x_candidate.sort(key=lambda x:x[1])
    for i in range(len(x_candidate) - 1):
        for j in range(i + 1, len(x_candidate)):
            if min_val > (x_candidate[i][1] - x_candidate[j][1]) ** 2:
                temp = min(temp, dist(x_candidate[i], x_candidate[j]))
            else:
                break
    return temp

def main():
    n = int(sys.stdin.readline().rstrip())
    dots = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
    dots.sort()
    ans = solve(dots, 0, n - 1)
    print(ans)
    return

if __name__ == "__main__":
    main()