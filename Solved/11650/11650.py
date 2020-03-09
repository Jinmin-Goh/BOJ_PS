# Problem No.: 11650
# Solver:      Jinmin Goh
# Date:        20200309
# URL: https://www.acmicpc.net/problem/11650

import sys

def main():
    n = int(input())
    ans = []
    for i in range(n):
        x, y = map(int, input().split())
        ans.append((x, y))
    ans.sort()
    for i in ans:
        print(i[0], i[1])
    return

if __name__ == "__main__":
    main()