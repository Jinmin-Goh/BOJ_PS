# Problem No.: 2108
# Solver:      Jinmin Goh
# Date:        20200313
# URL: https://www.acmicpc.net/problem/2108

import sys

def main():
    n = int(input())
    nums = []
    numDict = {}
    for i in range(n):
        temp = int(sys.stdin.readline())
        nums.append(temp)
        if temp not in numDict:
            numDict[temp] = 1
        else:
            numDict[temp] += 1
    modeVal = []
    modeCnt = 0
    for i in numDict:
        if numDict[i] > modeCnt:
            modeCnt = numDict[i]
            modeVal = [i]
        elif numDict[i] == modeCnt:
            modeVal.append(i)
    modeVal.sort()
    if len(modeVal) >= 2:
        modeVal = modeVal[1]
    else:
        modeVal = modeVal[0]
    meanVal = sum(nums) / n
    if meanVal - int(meanVal) >= 0.5:
        meanVal += 1
    if meanVal - int(meanVal) < -0.5:
        meanVal -= 1
    meanVal = int(meanVal)
    nums.sort()
    diffVal = nums[-1] - nums[0]
    medianVal = 0
    if n % 2:
        medianVal = nums[n // 2]
    else:
        medianVal = (nums[n // 2] + nums[n // 2 - 1]) / 2
    print(meanVal)
    print(medianVal)
    print(modeVal)
    print(diffVal)
    return

if __name__ == "__main__":
    main()