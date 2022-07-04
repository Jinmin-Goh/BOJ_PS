# Problem No.: 25321
# Solver:      Jinmin Goh
# Date:        20220704
# URL: https://www.acmicpc.net/problem/25321

import sys
sys.setrecursionlimit(400000)

f = [1]

def catalan(n):
    a = f[2 * n]
    b = f[n] * f[n + 1]
    b = pow(b, -1, 1000000007)
    return (a * b) % 1000000007

def solve(s):
    if s == []:
        return 1
    ret = catalan(len(s))
    for i in s:
        ret *= solve(i)
        ret %= 1000000007
    return ret % 1000000007

def main():
    s = sys.stdin.readline().rstrip()
    temp = []
    for i in s:
        if i == ':':
            temp.append('],')
        elif i == '?':
            temp.append('[')
    global f
    for i in range(1, 150001):
        f.append((f[-1] * i) % 1000000007)
    temp = ''.join(temp)[:-1]
    temp = eval(temp)
    ans = solve(temp)
    print(ans)
    return

if __name__ == "__main__":
    main()