# Problem No.: 16565
# Solver:      Jinmin Goh
# Date:        20220708
# URL: https://www.acmicpc.net/problem/16565

import sys

def combination(f, a, b):
    return (f[a] * pow(f[b], -1, 10007) * pow(f[a - b], -1, 10007)) % 10007

def main():
    n = int(input())
    f = [1]
    for i in range(52):
        f.append((f[-1] * (i + 1)) % 10007)
    pos_flag = True
    cnt = n // 4
    ans = 0
    for i in range(1, cnt + 1):
        if pos_flag:
            ans += combination(f, 13, i) * combination(f, 52 - 4 * i, n - 4 * i)
        else:
            ans -= combination(f, 13, i) * combination(f, 52 - 4 * i, n - 4 * i)
        pos_flag = not pos_flag
        ans %= 10007
    print(ans)
    return

if __name__ == "__main__":
    main()