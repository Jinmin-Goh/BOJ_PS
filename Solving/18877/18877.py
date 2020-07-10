# Problem No.: 18877
# Solver:      Jinmin Goh
# Date:        20200709
# URL: https://www.acmicpc.net/problem/18877

import sys

def main():
    n, m = map(int, input().split())
    area = []
    grassLen = 0
    for _ in range(m):
        area.append(tuple(map(int, sys.stdin.readline().split())))
        grassLen += area[-1][1] - area[1][0] + 1
    area.sort()

    if grassLen == n:
        ans = 10 ** 18
        for i in range(m):
            if area[i][1] - area[i][0] > 0:
                ans = 0
                break
            elif i > 0:
                ans = min(ans, area[i][0] - area[i - 1][1])
        print(ans)
        return
    

    

    return

if __name__ == "__main__":
    main()