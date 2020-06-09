# Problem No.: 2178
# Solver:      Jinmin Goh
# Date:        20200609
# URL: https://www.acmicpc.net/problem/2178

import sys
import collections

def main():
    n, m = map(int, input().split())
    graph = []
    for _ in range(n):
        temp = sys.stdin.readline().strip()
        graph.append([])
        for i in temp:
            graph[-1].append(int(i))
    stack = collections.deque([(0, 0)])
    #print(graph)
    flag = False
    ans = 0
    while stack:
        stack.append(None)
        ans += 1
        while True:
            temp = stack.popleft()
            if temp == None:
                break
            x, y = temp[0], temp[1]
            if graph[x][y] == -1:
                continue
            if x == n - 1 and y == m - 1:
                flag = True
                break
            if graph[x][y] == 1:
                if x > 0:
                    stack.append((x - 1, y))
                if x < n - 1:
                    stack.append((x + 1, y))
                if y > 0:
                    stack.append((x, y - 1))
                if y < m - 1:
                    stack.append((x, y + 1))
            graph[x][y] = -1
            
        if flag:
            break
    print(ans)
    
    return

if __name__ == "__main__":
    main()