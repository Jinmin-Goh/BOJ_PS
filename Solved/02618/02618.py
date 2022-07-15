# Problem No.: 2618
# Solver:      Jinmin Goh
# Date:        20220715
# URL: https://www.acmicpc.net/problem/2618

import sys
sys.setrecursionlimit(1000010)

def find(dp, case1, case2, car1, car2, w):
    if dp[car1][car2] != -1:
        return dp[car1][car2]
    if car1 == w or car2 == w:
        return 0
    next = max(car1, car2) + 1
    dist1 = abs(case1[car1][0] - case1[next][0]) + abs(case1[car1][1] - case1[next][1])
    dist2 = abs(case2[car2][0] - case2[next][0]) + abs(case2[car2][1] - case2[next][1])
    result1 = dist1 + find(dp, case1, case2, next, car2, w)
    result2 = dist2 + find(dp, case1, case2, car1, next, w)
    dp[car1][car2] = min(result1, result2)
    return dp[car1][car2]

def path(dp, case1, case2, car1, car2, w):
    if car1 == w or car2 == w:
        return
    next = max(car1, car2) + 1
    dist1 = abs(case1[car1][0] - case1[next][0]) + abs(case1[car1][1] - case1[next][1])
    dist2 = abs(case2[car2][0] - case2[next][0]) + abs(case2[car2][1] - case2[next][1])
    res1 = dist1 + dp[next][car2]
    res2 = dist2 + dp[car1][next]
    if res1 < res2:
        print(1)
        path(dp, case1, case2, next, car2, w)
    else:
        print(2)
        path(dp, case1, case2, car1, next, w)

def main():
    n = int(input())
    w = int(input())
    dp = [[-1 for _ in range(w + 2)] for _ in range(w + 2)]
    temp1 = [(1, 1)]
    temp2 = [(n, n)]
    dots = [tuple(map(int, sys.stdin.readline().split())) for _ in range(w)]
    case1 = temp1 + dots
    case2 = temp2 + dots
    print(find(dp, case1, case2, 0, 0, w))
    path(dp, case1, case2, 0, 0, w)
    return

if __name__ == "__main__":
    main()