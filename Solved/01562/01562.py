# Problem No.: 1562
# Solver:      Jinmin Goh
# Date:        20220620
# URL: https://www.acmicpc.net/problem/1562

import sys

def main():
    n = int(input())
    dp_table = [[[0 for _ in range(2 ** 10)] for __ in range(10)] for ___ in range(n)]
    for i in range(10):
        dp_table[0][i][2 ** i] = 1
    for i in range(1, n):
        for j in range(10):
            for k in range(2 ** 10):
                if j == 0:
                    dp_table[i][0][(2 ** 0) | k] = (dp_table[i][0][(2 ** 0) | k] + dp_table[i - 1][1][k]) % (10 ** 9)
                elif j == 9:
                    dp_table[i][9][(2 ** 9) | k] = (dp_table[i][9][(2 ** 9) | k] + dp_table[i - 1][8][k]) % (10 ** 9)
                else:
                    dp_table[i][j][(2 ** j) | k] = (dp_table[i][j][(2 ** j) | k] + dp_table[i - 1][j - 1][k] + dp_table[i - 1][j + 1][k]) % (10 ** 9)
    ans = 0
    for i in range(1, 10):
        ans += dp_table[-1][i][-1]
    ans %= 10 ** 9
    print(ans)
    return

if __name__ == "__main__":
    main()