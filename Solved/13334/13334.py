# Problem No.: 13334
# Solver:      Jinmin Goh
# Date:        20220707
# URL: https://www.acmicpc.net/problem/13334

import sys
import heapq

def main():
    n = int(input())
    lines = []
    for _ in range(n):
        a, b = map(int, sys.stdin.readline().split())
        if a > b:
            a, b = b, a
        lines.append((a, b))
    L = int(input())
    lines.sort(key=lambda x:(x[1], x[0]))
    pq = []
    cnt = 0
    max_val = 0
    for a, b in lines:
        cnt += 1
        heapq.heappush(pq, (a, b))
        while pq and pq[0][0] < b - L:
            heapq.heappop(pq)
            cnt -= 1
        max_val = max(max_val, cnt)        
    print(max_val)
    return

if __name__ == "__main__":
    main()