# Problem No.: 17401
# Solver:      Jinmin Goh
# Date:        20220804
# URL: https://www.acmicpc.net/problem/17401

import sys

def mul(arr1, arr2):
    n = len(arr1)
    arr = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            temp = 0
            for k in range(n):
                temp += (arr1[i][k] * arr2[k][j]) % 1000000007
            arr[i][j] = temp % 1000000007
    return arr

def main():
    t, n, d = map(int, sys.stdin.readline().split())
    arr_list = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(t)]
    arr_mul_list = [[[0 for _ in range(n)] for _ in range(n)]]
    for i in range(n):
        arr_mul_list[0][i][i] = 1
    for i in range(t):
        m = int(sys.stdin.readline().rstrip())
        for _ in range(m):
            a, b, c = map(int, sys.stdin.readline().split())
            arr_list[i][a - 1][b - 1] = c
        arr_mul_list.append(mul(arr_mul_list[-1], arr_list[i]))
    val = d // t
    remainder = d % t
    ans = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        ans[i][i] = 1
    temp = arr_mul_list[-1]
    while val:
        if val % 2:
            ans = mul(ans, temp)
        val >>= 1
        temp = mul(temp, temp)
    ans = mul(ans, arr_mul_list[remainder])
    for i in range(n):
        for j in range(n):
            print(ans[i][j], end=' ')
        print()
    return

if __name__ == "__main__":
    main()