# Problem No.: 1017
# Solver:      Jinmin Goh
# Date:        20220825
# URL: https://www.acmicpc.net/problem/1017

import sys

def dfs(graph, visited, directed, curr):
    for next in graph[curr]:
        if visited[next]:
            continue
        visited[next] = True
        if directed[next] == -1 or dfs(graph, visited, directed, directed[next]):
            directed[next] = curr
            return True
    return False

def main():
    n = int(sys.stdin.readline().rstrip())
    nums = list(map(int, sys.stdin.readline().split()))
    check = [False for _ in range(2010)]
    prime = set()
    for i in range(2, 2010):
        if not check[i]:
            prime.add(i)
            for j in range(i, 2010, i):
                check[j] = True
    graph = [[] for _ in range(n)]
    for i in range(n - 1):
        for j in range(i + 1, n):
            if nums[i] + nums[j] in prime:
                graph[i].append(j)
                graph[j].append(i)
    ans = []
    for i in graph[0]:
        directed = [-1 for _ in range(n)]
        cnt = 2
        directed[0] = i
        directed[i] = 0
        for j in range(1, n):
            visited = [False for _ in range(n)]
            visited[0] = True
            visited[i] = True
            if dfs(graph, visited, directed, j):
                cnt += 1
        if cnt == n:
            ans.append(nums[i])
    ans.sort()
    if not ans:
        print(-1)
    else:
        for i in ans:
            print(i, end=' ')
    return

if __name__ == "__main__":
    main()