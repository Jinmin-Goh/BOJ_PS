# Problem No.: 6086
# Solver:      Jinmin Goh
# Date:        20220830
# URL: https://www.acmicpc.net/problem/6086

import sys

def solve(graph, capacity, flow, s, t):
    ans = 0
    while True:
        parent = [-1 for _ in range(310)]
        queue = [s]
        while queue and parent[t] == -1:
            temp = []
            for curr in queue:
                for next in graph[curr]:
                    if capacity[curr][next] - flow[curr][next] > 0 and parent[next] == -1:
                        temp.append(next)
                        parent[next] = curr
            queue = temp
        if parent[t] == -1:
            break
        val = 10 ** 6
        curr = t
        while curr != s:
            val = min(val, capacity[parent[curr]][curr] - flow[parent[curr]][curr])
            curr = parent[curr]
        curr = t
        while curr != s:
            flow[parent[curr]][curr] += val
            flow[curr][parent[curr]] -= val
            curr = parent[curr]
        ans += val
    return ans

def main():
    n = int(sys.stdin.readline().rstrip())
    graph = [[] for _ in range(310)]
    flow = [[0 for _ in range(310)] for _ in range(310)]
    capacity = [[0 for _ in range(310)] for _ in range(310)]
    for _ in range(n):
        a, b, w = map(str, sys.stdin.readline().split())    
        a = ord(a) - ord('A')
        b = ord(b) - ord('A')
        graph[a].append(b)
        graph[b].append(a)
        capacity[a][b] += int(w)
        capacity[b][a] += int(w)
    ans = solve(graph, capacity, flow, 0, 25)
    print(ans)

    return

if __name__ == "__main__":
    main()