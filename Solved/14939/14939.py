# Problem No.: 14939
# Solver:      Jinmin Goh
# Date:        20220701
# URL: https://www.acmicpc.net/problem/14939

import sys

def change(table, i, j):
    table[i][j] = not table[i][j]
    if i > 0:
        table[i - 1][j] = not table[i - 1][j]
    if i < 9:
        table[i + 1][j] = not table[i + 1][j]
    if j > 0:
        table[i][j - 1] = not table[i][j - 1]
    if j < 9:
        table[i][j + 1] = not table[i][j + 1]

def main():
    table = [list(input()) for _ in range(10)]
    table = [[True if table[i][j] == 'O' else False for i in range(10)] for j in range(10)]
    ans = 1000
    for i in range(2 ** 10):
        min_val = 0
        cnt = 0
        temp = i
        temp_table = [[table[i][j] for i in range(10)] for j in range(10)]
        while temp:
            if temp % 2:
                change(temp_table, 0, cnt)
                min_val += 1
            cnt += 1
            temp //= 2
        for j in range(1, 10):
            for k in range(10):
                if temp_table[j - 1][k]:
                    change(temp_table, j, k)
                    min_val += 1
        flag = False
        for j in range(10):
            for k in range(10):
                if temp_table[j][k]:
                    flag = True
                    break
            if flag:
                break
        if not flag:
            ans = min(ans, min_val)
    print(ans)
    return

if __name__ == "__main__":
    main()