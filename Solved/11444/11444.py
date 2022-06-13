# Problem No.: 11444
# Solver:      Jinmin Goh
# Date:        20220613
# URL: https://www.acmicpc.net/problem/11444

import sys

def multiply(arr1, arr2):
    newArr = [[-1, -1],
              [-1, -1]]
    newArr[0][0] = (arr1[0][0] * arr2[0][0]) % 1000000007 + (arr1[0][1] * arr2[1][0]) % 1000000007
    newArr[0][1] = (arr1[0][0] * arr2[0][1]) % 1000000007 + (arr1[0][1] * arr2[1][1]) % 1000000007
    newArr[1][0] = (arr1[1][0] * arr2[0][0]) % 1000000007 + (arr1[1][1] * arr2[1][0]) % 1000000007
    newArr[1][1] = (arr1[1][0] * arr2[0][1]) % 1000000007 + (arr1[1][1] * arr2[1][1]) % 1000000007
    return newArr

def main():
    n = int(input())
    init = [[0, 1],
           [1, 1]]
    ans = [[1, 0],
           [0, 1]]
    while n > 0:
        if n % 2:
           ans = multiply(ans, init)
        init = multiply(init, init)
        n //= 2
    print(ans[0][1] % 1000000007)
    return

if __name__ == "__main__":
    main()