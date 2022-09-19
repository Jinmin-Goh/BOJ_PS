# Problem No.: 25622
# Solver:      Jinmin Goh
# Date:        20220919
# URL: https://www.acmicpc.net/problem/25622

import sys

def dfs(ans, graph, curr, parent):
    temp = []
    for next in graph[curr]:
        if next == parent:
            continue
        val = dfs(ans, graph, next, curr)
        if val == -1:
            return -1
        else:
            temp += val
    if len(temp) == 2:
        temp.append(curr)
        ans.append(temp)
        return []
    elif len(temp) > 2:
        return -1
    else:
        temp.append(curr)
        return temp


def main():
    n = int(sys.stdin.readline().rstrip())
    graph = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)
    ans = []
    val = dfs(ans, graph, 1, 0)
    if val == -1:
        print('U')
    else:
        print('S')
        for a, b, c in ans:
            print(a, b, c)
    return

if __name__ == "__main__":
    main()