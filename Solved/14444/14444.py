# Problem No.: 14444
# Solver:      Jinmin Goh
# Date:        20220823
# URL: https://www.acmicpc.net/problem/14444

import sys

def main():
    temp = sys.stdin.readline().rstrip()
    s = []
    for i in range(len(temp) * 2 + 1):
        if i % 2:
            s.append(temp[i // 2])
        else:
            s.append('.')
    ''.join(s)
    n = len(s)
    r = 0
    p = 0
    ans_list = [0 for _ in range(n)]
    for i in range(n):
        if i <= r:
            ans_list[i] = min(ans_list[2 * p - i], r - i)
        else:
            ans_list[i] = 0
        while i - ans_list[i] - 1 >= 0 and i + ans_list[i] + 1 < n and s[i - ans_list[i] - 1] == s[i + ans_list[i] + 1]:
            ans_list[i] += 1
        if r < i + ans_list[i]:
            r = i + ans_list[i]
            p = i
    ans = 0
    for i in range(n):
        ans = max(ans, ans_list[i])
    print(ans)
    return

if __name__ == "__main__":
    main()