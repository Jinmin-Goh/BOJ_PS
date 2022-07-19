# Problem No.: 1019
# Solver:      Jinmin Goh
# Date:        20220719
# URL: https://www.acmicpc.net/problem/1019

import sys

def solve(cnt, n):
    if n == 0:
        return [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ans = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    l = len(str(n))
    top = n // (10 ** (l - 1))
    if l == 1:
        for i in range(1, top + 1):
            ans[i] += 10 ** (l - 1)
    else:
        for i in range(1, top):
            ans[i] += 10 ** (l - 1)
        ans[top] += n % (10 ** (l - 1)) + 1
        for i in range(1, 10):
            ans[i] += cnt[l - 1] * (top - 1)
    temp1 = solve(cnt, n % (10 ** (l - 1)))
    temp2 = solve(cnt, 10 ** (l - 1) - 1)
    for i in range(10):
        ans[i] += temp1[i] + temp2[i]
    return ans

def main():
    n = int(input())
    cnt = [i * (10 ** (i - 1)) for i in range(15)]
    cnt[0] = 0
    ans = solve(cnt, n)
    l = len(str(n))
    sum_val = sum(ans)
    ans[0] = (l * n) - sum_val
    for i in range(1, l):
        ans[0] -= (l - i) * 9 * (10 ** (i - 1))
    for i in ans:
        print(i, end=" ")
    return

if __name__ == "__main__":
    main()