# Problem No.: 13263
# Solver:      Jinmin Goh
# Date:        20220805
# URL: https://www.acmicpc.net/problem/13263

import sys

def main():
    n = int(sys.stdin.readline().rstrip())
    a = list(map(int, sys.stdin.readline().split()))
    b = list(map(int, sys.stdin.readline().split()))
    dp = [0 for _ in range(n)]
    lines = [[1, 0, 0] for _ in range(n)]
    top = 0
    temp = None
    for i in range(n - 1):
        temp = [b[i], dp[i], 0]
        while top > 0:
            temp[2] = (temp[1] - lines[top - 1][1]) / (lines[top - 1][0] - temp[0])
            if lines[top - 1][2] < temp[2]:
                break
            top -= 1
        lines[top] = temp
        top += 1
        x = a[i + 1]
        line_pos = top - 1
        if x < lines[top - 1][2]:
            l = 0
            r = top - 1
            while l < r:
                m = (l + r) // 2
                if x < lines[m][2]:
                    r = m
                else:
                    l = m + 1
            line_pos = l - 1
        dp[i + 1] = lines[line_pos][0] * x + lines[line_pos][1]
        print(lines)
    print(dp[-1])

    return

if __name__ == "__main__":
    main()