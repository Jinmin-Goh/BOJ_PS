# Problem No.: 2263
# Solver:      Jinmin Goh
# Date:        20200415
# URL: https://www.acmicpc.net/problem/2263

import sys

sys.setrecursionlimit(10 ** 8)

inorderList = None
postorderList = None

## need to change list to coordinate
def preorder(inFront: int, inRear: int, postFront: int, postRear: int) -> [int]:
    #print(inFront, inRear, postFront, postRear)
    if inFront > inRear or postFront > postRear or 0 > inRear or inFront >= len(inorderList) or postRear < 0 or postFront >= len(postorderList):
        return []
    if inFront == inRear:
        return [inorderList[inFront]]
    head = postorderList[postRear]
    inHeadPos = inorderList.index(head)
    
    left = preorder(inFront, inHeadPos - 1, postFront, postFront + (inHeadPos - inFront) - 1)
    right = preorder(inHeadPos + 1, inRear, postFront + (inHeadPos - inFront), postRear - 1)
    return [head] + left + right

def main():
    n = int(input())
    global inorderList
    global postorderList
    inorderList = list(map(int, sys.stdin.readline().split()))
    postorderList = list(map(int, sys.stdin.readline().split()))
    if n == 1:
        print(inorderList[0])
        return
    ans = preorder(0, n - 1, 0, n - 1)
    #print(ans)
    for i in ans:
        print(i, end = " ")
    return

if __name__ == "__main__":
    main()