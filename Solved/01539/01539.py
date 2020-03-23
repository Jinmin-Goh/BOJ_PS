# Problem No.: 1539
# Solver:      Jinmin Goh
# Date:        20200324
# URL: https://www.acmicpc.net/problem/1539

import sys

def main():
    n = int(input())
    ans = 0
    nums = []
    for _ in range(n):
        nums.append(int(sys.stdin.readline()))
    # used doublely linked list implemented with list for pointer
    LList = [None] * n
    for i in range(1, n):
        LList[i] = i - 1
    RList = [None] * n
    for i in range(n - 1):
        RList[i] = i + 1
    numPosList = [[None, None] for _ in range(n)]
    for i in reversed(nums):
        numPosList[i][0] = LList[i]
        numPosList[i][1] = RList[i]
        tempL = LList[i]
        tempR = RList[i]
        if tempR != None:
            LList[tempR] = LList[i]
        if tempL != None:
            RList[tempL] = RList[i]
    numHelghtList = [None] * n
    for i in nums:
        if numPosList[i][0] == None and numPosList[i][1] == None:
            numHelghtList[i] = 1
        elif numPosList[i][0] == None:
            numHelghtList[i] = numHelghtList[numPosList[i][1]] + 1
        elif numPosList[i][1] == None:
            numHelghtList[i] = numHelghtList[numPosList[i][0]] + 1
        else:
            numHelghtList[i] = max(numHelghtList[numPosList[i][0]], numHelghtList[numPosList[i][1]]) + 1
        ans += numHelghtList[i]
    print(ans)
    return

if __name__ == "__main__":
    main()