# Problem No.: 1948
# Solver:      Jinmin Goh
# Date:        20220713
# URL: https://www.acmicpc.net/problem/1948

import sys

def main():
    n = int(sys.stdin.readline().rstrip())
    m = int(sys.stdin.readline().rstrip())
    graph = [[] for _ in range(n + 1)]
    degree = [0 for _ in range(n + 1)]
    for _ in range(m):
        a, b, w = map(int, sys.stdin.readline().split())
        graph[a].append((b, w))
        degree[b] += 1
    s, e = map(int, sys.stdin.readline().split())
    stack = [s]
    topological_sorting = []
    while stack:
        temp = []
        for curr in stack:
            if degree[curr] == 0:
                topological_sorting.append(curr)
            for i in range(len(graph[curr])):
                next, _ = graph[curr][i]
                degree[next] -= 1
                if degree[next] == 0:
                    stack.append(next)
        stack = temp
    max_cost = [0 for _ in range(n + 1)]
    new_graph = [{} for _ in range(n + 1)]
    for curr in topological_sorting:
        for i in range(len(graph[curr])):
            next, w = graph[curr][i]
            if max_cost[next] == max_cost[curr] + w:
                new_graph[next].add(curr)
            elif max_cost[next] < max_cost[curr] + w:
                new_graph[next] = {curr}
                max_cost[next] = max_cost[curr] + w
            temp.append(next)
    print(max_cost[e])
    new_graph = [list(i) for i in new_graph]
    stack = [e]
    ans = 0
    visited_set = set()
    while stack:
        temp = []
        for curr in stack:
            if curr == s:
                continue
            for next in new_graph[curr]:
                if (curr, next) not in visited_set:
                    ans += 1
                    visited_set.add((curr, next))
                    temp.append(next)
        stack = temp
    print(ans)
    return

if __name__ == "__main__":
    main()