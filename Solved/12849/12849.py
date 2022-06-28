# Problem No.: 12849
# Solver:      Jinmin Goh
# Date:        20220628
# URL: https://www.acmicpc.net/problem/12849

import sys

def multiple(arr1, arr2):
    n = len(arr1)
    new_arr = [[0 for _ in range(n)] for __ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                new_arr[i][j] += arr1[i][k] * arr2[k][j]
                new_arr[i][j] %= 1000000007
    return new_arr

def main():
    n = int(input())
    array = [[0, 1, 1, 0, 0, 0, 0, 0],
             [1, 0, 1, 1, 0, 0, 0, 0],
             [1, 1, 0, 1, 1, 0, 0, 0],
             [0, 1, 1, 0, 1, 1, 0, 0],
             [0, 0, 1, 1, 0, 1, 1, 0],
             [0, 0, 0, 1, 1, 0, 0, 1],
             [0, 0, 0, 0, 1, 0, 0, 1],
             [0, 0, 0, 0, 0, 1, 1, 0]]
    ans = [[1, 0, 0, 0, 0, 0, 0, 0],
           [0, 1, 0, 0, 0, 0, 0, 0],
           [0, 0, 1, 0, 0, 0, 0, 0],
           [0, 0, 0, 1, 0, 0, 0, 0],
           [0, 0, 0, 0, 1, 0, 0, 0],
           [0, 0, 0, 0, 0, 1, 0, 0],
           [0, 0, 0, 0, 0, 0, 1, 0],
           [0, 0, 0, 0, 0, 0, 0, 1]]
    while n:
        if n % 2:
            ans = multiple(ans, array)
        n //= 2
        array = multiple(array, array)
    print(ans[0][0] % 1000000007)
    return

if __name__ == "__main__":
    main()