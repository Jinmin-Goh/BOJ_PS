# Problem No.: 3495
# Solver:      Jinmin Goh
# Date:        20200512
# URL: https://www.acmicpc.net/problem/3495

import sys

def main():
    n, m = map(int, sys.stdin.readline().split())
    graph = []
    for _ in range(n):
        graph.append(sys.stdin.readline().strip())
    ans = 0
    for i in range(n):
        flag = False
        for j in range(m):
            if graph[i][j] in ["/", "\\"]:
                flag = not flag
                ans += 0.5
            else:
                if flag:
                    ans += 1
    print(int(ans))

    return

if __name__ == "__main__":
    main()