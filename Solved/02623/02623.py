# Problem No.: 2623
# Solver:      Jinmin Goh
# Date:        20220624
# URL: https://www.acmicpc.net/problem/2623

import sys

def main():
    n, m = map(int, input().split())
    cnt = [0 for _ in range(n + 1)]
    graph = {i:[] for i in range(1, n + 1)}
    for _ in range(m):
        temp = list(map(int, sys.stdin.readline().split()))
        for i in range(1, temp[0]):
            graph[temp[i]].append(temp[i + 1])
            cnt[temp[i + 1]] += 1
    queue = []
    for i in range(1, n + 1):
        if cnt[i] == 0:
            queue.append(i)
    ans = []
    while queue:
        temp = []
        for curr in queue:
            if cnt[curr] == 0:
                ans.append(curr)
            for next in graph[curr]:
                cnt[next] -= 1
                if cnt[next] == 0:
                    temp.append(next)
        queue = temp
    if len(ans) != n:
        print(0)
    else:
        for i in ans:
            print(i)
    return

if __name__ == "__main__":
    main()