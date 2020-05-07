# Problem No.: 11725
# Solver:      Jinmin Goh
# Date:        20200508
# URL: https://www.acmicpc.net/problem/11725

import sys

def main():
    n = int(input())
    treeList = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        a, b = map(int, sys.stdin.readline().split())
        treeList[a].append(b)
        treeList[b].append(a)
    parentList = [None] * (n + 1)
    stack = [1]
    visitedSet = set()
    while stack:
        node = stack.pop(0)
        if node in visitedSet:
            continue
        visitedSet.add(node)
        for i in treeList[node]:
            if i in visitedSet:
                continue
            parentList[i] = node
            stack.append(i)
    for i in range(2, n + 1):
        print(parentList[i])
    return

if __name__ == "__main__":
    main()