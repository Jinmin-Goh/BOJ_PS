# Problem No.: 1533
# Solver:      Jinmin Goh
# Date:        20220801
# URL: https://www.acmicpc.net/problem/1533

import sys

def mul(a, b):
    n = len(a)
    new_arr = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            temp = 0
            for k in range(n):
                temp += (a[i][k] * b[k][j]) % 1000003
            new_arr[i][j] = temp % 1000003
    return new_arr

def main():
    n, s, e, t = map(int, sys.stdin.readline().split())
    arr =[[0 for _ in range(5 * n + 1)] for _ in range(5 * n + 1)]
    for i in range(n):
        temp = list(map(int, list(sys.stdin.readline().rstrip())))
        for j in range(n):
            if temp[j] > 0:
                arr[5 * (i + 1)][5 * (j + 1) - (temp[j] - 1)] = 1
        for j in range(1, 5):
            arr[5 * i + j][5 * i + j + 1] = 1
    ans = [[0 for _ in range(5 * n + 1)] for _ in range(5 * n + 1)]
    for i in range(5 * n + 1):
        ans[i][i] = 1
    while t:
        if t % 2:
            ans = mul(ans, arr)
        arr = mul(arr, arr)
        t >>= 1
    print(ans[5 * s][5 * e])
            
    return

if __name__ == "__main__":
    main()