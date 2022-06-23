# Problem No.: 2252
# Solver:      Jinmin Goh
# Date:        20220623
# URL: https://www.acmicpc.net/problem/2252

import sys

def main():
    n, m = map(int, input().split())
    cnt = [0 for _ in range(n)]
    graph = {i: [] for i in range(n)}
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        cnt[b - 1] += 1
        graph[a - 1].append(b - 1)
    queue = []
    for i in range(n):
        if cnt[i] == 0:
            queue.append(i)
    ans = []
    while queue:
        temp = []
        for curr in queue:
            if cnt[curr] == 0:
                ans.append(curr + 1)
            for next in graph[curr]:
                cnt[next] -= 1
                if cnt[next] == 0:
                    temp.append(next)
        queue = temp
    for node in ans:
        print(node, end=" ")
    return

if __name__ == "__main__":
    main()