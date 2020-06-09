# Problem No.: 1389
# Solver:      Jinmin Goh
# Date:        20200609
# URL: https://www.acmicpc.net/problem/1389

import sys
import collections

def main():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)
    ans = None
    minVal = m * n
    for i in range(1, n + 1):
        stack = collections.deque([i])
        visited = [False] * (n + 1)
        cnt = 0
        sumVal = 0
        while stack:
            stack.append(None)
            while True:
                temp = stack.popleft()
                if temp == None:
                    break
                if visited[temp]:
                    continue
                visited[temp] = True
                sumVal += cnt
                stack += graph[temp]
            cnt += 1
        #print(minVal, sumVal, i)
        if minVal > sumVal:
            minVal = sumVal
            ans = i
    print(ans)
            

    return

if __name__ == "__main__":
    main()