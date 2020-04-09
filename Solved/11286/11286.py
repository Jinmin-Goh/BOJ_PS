# Problem No.: 11286
# Solver:      Jinmin Goh
# Date:        20200410
# URL: https://www.acmicpc.net/problem/11286

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
                temp = heapq.heappop(heap) 
                print(temp[1])
        else:
            heapq.heappush(heap, (abs(num),num))
    return

if __name__ == "__main__":
    main()