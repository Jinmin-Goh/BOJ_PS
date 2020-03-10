# Problem No.: 1256
# Solver:      Jinmin Goh
# Date:        20200310
# URL: https://www.acmicpc.net/problem/1256

import sys

def main():
    n, m, k = map(int, input().split())
    comb = [[0] * (n + m + 1) for i in range(n + m + 1)]
    for i in range(n + m + 1):
        comb[i][0] = 1
    for i in range(1, n + m + 1):
        for j in range(i + 1):
            comb[i][j] = comb[i - 1][j] + comb[i - 1][j - 1]
    if k > comb[n + m][n]:
        print(-1)
        return
    if n == 0:
        print("z" * m)
        return
    if m == 0:
        print("a" * n)
        return
    ans = ""
    cnt = 0
    length = m + n
    while length > cnt:
        if k > comb[m + n - 1][m]:
            k -= comb[m + n - 1][m]
            ans += "z"
            cnt += 1
            m -= 1
        else:
            ans += "a"
            cnt += 1
            n -= 1
    print(ans)    
    return

if __name__ == "__main__":
    main()