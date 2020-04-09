# Problem No.: 1927
# Solver:      Jinmin Goh
# Date:        20200410
# URL: https://www.acmicpc.net/problem/1927

import heapq
import sys

def main():
    n = int(input())
    heap = []
    for _ in range(n):
        num = int(sys.stdin.readline().strip())
        if num == 0:
            if not heap:
                print(0)
            else:
                print(heapq.heappop(heap))
        else:
            heapq.heappush(heap, num)
    return

if __name__ == "__main__":
    main()