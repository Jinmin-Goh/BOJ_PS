# Problem No.: 2606
# Solver:      Jinmin Goh
# Date:        20200606
# URL: https://www.acmicpc.net/problem/2606

import sys

def main():
    n = int(input())
    m = int(input())
    graph = {}
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)
    visited = set()
    ans = 0
    stack = [1]
    while stack:
        temp = stack.pop()
        if temp in visited:
            continue
        visited.add(temp)
        ans += 1
        stack += graph[temp]
    print(ans - 1)
    return

if __name__ == "__main__":
    main()