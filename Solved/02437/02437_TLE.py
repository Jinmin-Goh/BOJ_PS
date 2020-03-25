# Problem No.: 2437
# Solver:      Jinmin Goh
# Date:        20200325
# URL: https://www.acmicpc.net/problem/2437

import sys

def check(weightList: [bool], numDict: {int:int}, target: int) -> bool:
    if target in numDict and numDict[target] > 0:
        return True
    flag = False
    for i in numDict:
        if i > target:
            continue
        if numDict[i] == 0:
            continue
        numDict[i] -= 1
        flag = check(weightList, numDict, target - i)
        numDict[i] += 1
        if flag:
            return True
    return False

def main():
    n = int(input())
    nums = list(map(int, sys.stdin.readline().split()))
    numDict = {}
    sumVal = n * (n + 1) // 2
    weightList = [False] * (sumVal + 1)
    weightList[0] = True
    nums.sort()
    nums = list(reversed(nums))
    for i in nums:
        if i not in numDict:
            numDict[i] = 1
            if i <= sumVal:
                weightList[i] = True
        else:
            numDict[i] += 1
    for i in range(1,sumVal + 1):
        #print(numDict, i)
        if not weightList[i]:
            flag = False
            for j in numDict:
                if j > i:
                    continue
                target = i - j
                numDict[j] -= 1
                flag = check(weightList, numDict, target)
                numDict[j] += 1
                if flag:
                    break
            if not flag:
                print(i)
                return
    print(sumVal + 1)
    return

if __name__ == "__main__":
    main()