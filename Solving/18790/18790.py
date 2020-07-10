# Problem No.: 18790
# Solver:      Jinmin Goh
# Date:        20200314
# URL: https://www.acmicpc.net/problem/18790

# currently TLE at 26%

import sys

notAnsSet = set()

def DFS(n: int, temp: int, numDict: {int:int}, ansDict = {int:int}) -> {int:int}:
    #print(temp, numDict, ansDict)
    if sum(list(ansDict.values())) == n and temp == 0:
        return ansDict
    tempTuple = []
    for j in ansDict:
        tempTuple.append((j, ansDict[j]))
    tempTuple.sort()
    tempTuple = tuple(tempTuple)
    if sum(list(ansDict.values())) >= n or tempTuple in notAnsSet:
        return
    for i in numDict:
        if numDict[i] == 0:
            continue
        else:
            #print(i, (temp - i) % n)
            numDict[i] -= 1
            ansDict[i] += 1
            tempDict = {}
            for j in ansDict:
                tempDict[j] = ansDict[j]
            tempAns = DFS(n, (temp - i) % n, numDict, tempDict)
            if tempAns:
                return tempAns
            tempTuple = []
            for j in tempDict:
                tempTuple.append((j, tempDict[j]))
            tempTuple.sort()
            tempTuple = tuple(tempTuple)
            notAnsSet.add(tempTuple)
            numDict[i] += 1
            ansDict[i] -= 1
            #print(tempAns)

def main():
    n = int(input())
    if n == 1:
        print(int(input()))
        return
    nums = list(map(int, sys.stdin.readline().split()))
    numDict = {}
    for i in nums:
        if i not in numDict:
            numDict[i] = 1
        else:
            numDict[i] += 1
            if numDict[i] == n:
                ans = [i] * n
                for j in ans:
                    print(j, end = " ")
                    return
    ansDict = {}
    for i in range(n):
        ansDict[i] = 0   
    for i in numDict:
        numDict[i] -= 1
        ansDict[i] += 1
        ans = DFS(n, n - i, numDict, ansDict)
        numDict[i] += 1
        ansDict[i] -= 1
        if ans:
            break
    #print(ans)
    for i in ans:
        for j in range(ans[i]):
            print(i, end = " ")
    return

if __name__ == "__main__":
    main()