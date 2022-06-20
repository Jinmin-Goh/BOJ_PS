# Problem No.: 1005
# Solver:      Jinmin Goh
# Date:        20220620
# URL: https://www.acmicpc.net/problem/1005

import sys

def main():
    t = int(input())
    for _ in range(t):
        # parsing
        n, k = map(int, sys.stdin.readline().split())
        time = list(map(int, sys.stdin.readline().split()))
        direction = [[False for __ in range(n + 1)] for ___ in range(n + 1)]
        cnt = [0 for __ in range(n + 1)]
        for __ in range(k):
            a, b = map(int, sys.stdin.readline().split())
            direction[a][b] = True
            cnt[b] += 1
        w = int(sys.stdin.readline())
        # find starting node
        queue = []
        for i in range(1, n + 1):
            if cnt[i] == 0:
                queue.append(i)
        total_time = [-1 for _ in range(n + 1)]
        for node in queue:
            total_time[node] = time[node - 1]
        while queue:
            temp = []
            for node in queue:
                for i in range(1, n + 1):
                    if i == node:
                        continue
                    
                    if direction[node][i]:
                        cnt[i] -= 1
                        if cnt[i] == 0:
                            temp.append(i)
                        total_time[i] = max(total_time[i], total_time[node] + time[i - 1])
            queue = temp
        ans = total_time[w]
        print(ans)

        
    return

if __name__ == "__main__":
    main()