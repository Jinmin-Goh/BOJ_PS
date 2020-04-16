# Problem No.: 2263
# Solver:      Jinmin Goh
# Date:        20200415
# URL: https://www.acmicpc.net/problem/2263

import sys

sys.setrecursionlimit(10 ** 8)

inorderDict = []
postorderList = []
inorderDict = {}
#postorderDict = {}

## need to change list to coordinate
def preorder(inFront: int, inRear: int, postFront: int, postRear: int) -> None:
    if inFront > inRear or postFront > postRear or 0 > inRear or inFront >= len(inorderList) or postRear < 0 or postFront >= len(postorderList):
        return
    if inFront == inRear:
        print(inorderList[inFront], end = " ")
        return
    head = postorderList[postRear]
    print(head, end = " ")
    inHeadPos = inorderDict[head]
    preorder(inFront, inHeadPos - 1, postFront, postFront + (inHeadPos - inFront) - 1)
    preorder(inHeadPos + 1, inRear, postFront + (inHeadPos - inFront), postRear - 1)

def main():
    n = int(input())
    global inorderDict
    #global postorderDict
    global inorderList
    global postorderList
    inorderList = list(map(int, sys.stdin.readline().split()))
    postorderList = list(map(int, sys.stdin.readline().split()))
    
    if n == 1:
        print(inorderList[0])
        return

    for i in range(len(inorderList)):
        inorderDict[inorderList[i]] = i
    #for i in range(len(postorderList)):
    #    inorderDict[postorderList[i]] = i
    
    preorder(0, n - 1, 0, n - 1)
    return

if __name__ == "__main__":
    main()