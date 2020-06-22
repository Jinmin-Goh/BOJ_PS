# Problem No.: 15686
# Solver:      Jinmin Goh
# Date:        20200622
# URL: https://www.acmicpc.net/problem/15686

import sys
import itertools

def main():
    n, m = map(int, input().split())
    table = []
    for _ in range(n):
        table.append(list(map(int, sys.stdin.readline().split())))
    house = []
    store = []
    for i in range(n):
        for j in range(n):
            if table[i][j] == 1:
                house.append([i, j])
            if table[i][j] == 2:
                store.append([i, j])
    
    ans = sys.maxsize
    combList = list(itertools.combinations(store, m))
    for storeList in combList:
        cost = 0
        for ho in house:
            temp = sys.maxsize
            for st in storeList:
                temp = min(temp, abs(st[0] - ho[0]) + abs(st[1] - ho[1]))
            cost += temp
        ans = min(ans, cost)

    print(ans)
    return

if __name__ == "__main__":
    main()