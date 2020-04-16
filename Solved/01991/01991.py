# Problem No.: 1991
# Solver:      Jinmin Goh
# Date:        20200416
# URL: https://www.acmicpc.net/problem/1991

import sys

def search(head: str, treeDict: {}) -> [str]:
    if treeDict[head] == [".", "."]:
        return [[head], [head], [head]]
    left = [[],[],[]]
    right = [[],[],[]]
    if treeDict[head][0] != ".":
        left = search(treeDict[head][0], treeDict)
    if treeDict[head][1] != ".":
        right = search(treeDict[head][1], treeDict)
    preList = [head] + left[0] + right[0]
    inList = left[1] + [head] + right[1]
    postList = left[2] + right[2] + [head]
    return [preList, inList, postList]
        

def main():
    n = int(input())
    treeDict = {}
    head = None
    for _ in range(n):
        root, left, right = map(str, sys.stdin.readline().split())
        if _ == 0:
            head = root
        treeDict[root] = [left, right]
    ans = search(head, treeDict)
    for i in ans:
        for j in i:
            print(j, end = "")
        print("")
    return

if __name__ == "__main__":
    main()