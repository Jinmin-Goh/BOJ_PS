# Problem No.: 13549
# Solver:      Jinmin Goh
# Date:        20200417
# URL: https://www.acmicpc.net/problem/13549

import sys

def main():
    n, k = map(int, input().split())
    if n >= k:
        print(n - k)
        return
    
    # 0-1 BFS
    deque = [n]
    cost = [None] * 100001
    cost[n] = 0
    while True:
        tempZero = []
        tempOne = []
        while deque:
            temp = deque.pop(0)
            if temp == k:
                print(cost[k])
                return
            if 2 * temp <= 100000 and cost[2 * temp] == None:
                cost[2 * temp] = cost[temp]
                tempZero.append(2 * temp)
            if temp + 1 <= 100000 and cost[temp + 1] == None:
                cost[temp + 1] = cost[temp] + 1
                tempOne.append(temp + 1)
            if temp - 1 >= 0 and cost[temp - 1] == None:
                cost[temp - 1] = cost[temp] + 1
                tempOne.append(temp - 1)
        deque = tempZero + tempOne

    return

if __name__ == "__main__":
    main()