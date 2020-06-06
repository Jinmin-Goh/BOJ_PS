# Problem No.: 11724
# Solver:      Jinmin Goh
# Date:        20200606
# URL: https://www.acmicpc.net/problem/11724

import sys

def main():
    n, m = map(int, input().split())
    graph = {}
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)
    visited = set()
    ans = 0
    for node in range(1, n + 1):
        if node in visited:
            continue
        ans += 1
        stack = [node]
        while stack:
            temp = stack.pop()
            if temp in visited:
                continue
            visited.add(temp)
            stack += graph[temp]
    print(ans)
    return

if __name__ == "__main__":
    main()