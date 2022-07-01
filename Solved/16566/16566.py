# Problem No.: 16566
# Solver:      Jinmin Goh
# Date:        20220701
# URL: https://www.acmicpc.net/problem/16566

import sys

def union(parent, x, y):
    x = find(parent, x)
    y = find(parent, y)
    if x == y:
        return
    if x < y:
        parent[x] = y
    else:
        parent[y] = x

def find(parent, x):
    if parent[x] == -1:
        return -1
    if parent[x] == x:
        return x
    parent[x] = find(parent, parent[x])
    return parent[x]

def main():
    n, m, k = map(int, input().split())
    cards = list(map(int, sys.stdin.readline().split()))
    discard = list(map(int, sys.stdin.readline().split()))
    cards.sort()
    parent = [-1 for _ in range(m)]
    ans = []
    for target in discard:
        pf = 0
        pr = m - 1
        while pf < pr:
            pm = (pf + pr) // 2
            if cards[pm] <= target:
                pf = pm + 1
            else:
                pr = pm
        val = find(parent, pf)
        if val == -1:
            parent[pf] = pf
            ans.append(cards[pf])
            if pf > 0 and find(parent, pf - 1) != -1:
                union(parent, pf - 1, pf)
            if pf < m - 1 and find(parent, pf + 1) != -1:
                union(parent, pf + 1, pf)
        else:
            ans.append(cards[val + 1])
            parent[val + 1] = val + 1
            parent[val] = val + 1
            if val < m - 2 and find(parent, val + 2) != -1:
                union(parent, val + 1, val + 2)
    for i in ans:
        print(i)
    return

if __name__ == "__main__":
    main()