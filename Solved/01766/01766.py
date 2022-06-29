# Problem No.: 1766
# Solver:      Jinmin Goh
# Date:        20220629
# URL: https://www.acmicpc.net/problem/1766

import sys
import heapq

def main():
    n, m = map(int, input().split())
    cnt = [0 for _ in range(n)]
    graph = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        graph[a - 1].append(b - 1)
        cnt[b - 1] += 1
    pq = []
    for i in range(n):
        if cnt[i] == 0:
            heapq.heappush(pq, i)
    ans = []
    while pq:
        curr = heapq.heappop(pq)
        ans.append(curr)
        for next in graph[curr]:
            cnt[next] -= 1
            if cnt[next] == 0:
                heapq.heappush(pq, next)
    for i in ans:
        print(i + 1, end=' ')
    return    

if __name__ == "__main__":
    main()