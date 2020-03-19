# Problem No.: 10830
# Solver:      Jinmin Goh
# Date:        20200319
# URL: https://www.acmicpc.net/problem/10830

import sys

def main():
    n, b = map(int, input().split())
    matrix = []
    for i in range(n):
        matrix.append(list(map(int, input().split())))
    ans = [[0] * n for _ in range(n)]
    for i in range(n):
        ans[i][i] = 1
    while b > 0:
        temp = [[0] * n for i in range(n)]
        if b % 2:
            for i in range(n):
                for j in range(n):
                    for k in range(n):
                        temp[i][j] += ans[i][k] * matrix[k][j]
            for i in range(n):
                for j in range(n):
                    ans[i][j] = temp[i][j] % 1000
        temp = [[0] * n for i in range(n)]
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    temp[i][j] += matrix[i][k] * matrix[k][j]
        for i in range(n):
            for j in range(n):
                matrix[i][j] = temp[i][j] % 1000
        b >>= 1
        
    for i in range(n):
        for j in range(n):
            print(ans[i][j], end = " ")
        print("")
    return

if __name__ == "__main__":
    main()