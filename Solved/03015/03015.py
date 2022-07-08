# Problem No.: 3015
# Solver:      Jinmin Goh
# Date:        20220708
# URL: https://www.acmicpc.net/problem/3015

import sys

def main():
    n = int(input())
    stack = []
    ans = 0
    for _ in range(n):
        num = int(sys.stdin.readline())
        if not stack:
            stack.append([num, 1])
            continue
        while stack and stack[-1][0] < num:
            ans += stack[-1][1]
            stack.pop()
        val = 1
        if stack and stack[-1][0] == num:
            val += stack[-1][1]
            ans += stack[-1][1]
            stack.pop()
        if stack:
            ans += 1
        stack.append([num, val])
    print(ans)
    return

if __name__ == "__main__":
    main()