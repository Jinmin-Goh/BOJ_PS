# Problem No.: 11049
# Solver:      Jinmin Goh
# Date:        20220616
# URL: https://www.acmicpc.net/problem/11049

import sys

def solve(arr, mem, p1, p2):
    if p2 - p1 == 1:
        mem[p1][p2] = arr[p1][0] * arr[p1][1] * arr[p2][1]
        return mem[p1][p2]
    minVal = 2 ** 31
    for i in range(p2 - p1):
        if i == 0:
            if mem[p1 + 1][p2] == 2 ** 31:
                mem[p1 + 1][p2] = solve(arr, mem, p1 + 1, p2)
            minVal = min(minVal, arr[p1][0] * arr[p1][1] * arr[p2][1] + mem[p1 + 1][p2])
        elif i == p2 - p1 - 1:
            if mem[p1][p2 - 1] == 2 ** 31:
                mem[p1][p2 - 1] = solve(arr, mem, p1, p2 - 1)
            minVal = min(minVal, mem[p1][p2 - 1] + arr[p1][0] * arr[p2][0] * arr[p2][1])
        else:
            if mem[p1][p1 + i] == 2 ** 31:
                mem[p1][p1 + i] = solve(arr, mem, p1, p1 + i) 
            if mem[p1 + i + 1][p2] == 2 ** 31:
                mem[p1 + i + 1][p2] = solve(arr, mem, p1 + i + 1, p2)
            minVal = min(minVal, arr[p1][0] * arr[p1 + i][1] * arr[p2][1] + mem[p1][p1 + i] + mem[p1 + i + 1][p2])
    mem[p1][p2] = minVal
    return mem[p1][p2]

def main():
    arr = []
    n = int(input())
    for _ in range(n):
        a, b = map(int, input().split())
        arr.append((a, b))
    mem = [[2 ** 31 for _ in range(n)] for __ in range(n)]
    ans = solve(arr, mem, 0, n - 1)
    print(ans)
    return

if __name__ == "__main__":
    main()