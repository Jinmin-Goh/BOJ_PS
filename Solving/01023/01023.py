# Problem No.: 1023
# Solver:      Jinmin Goh
# Date:        20200314
# URL: https://www.acmicpc.net/problem/1023

import sys

def main():
    n, k = map(int, input().split())
    if n % 2:
        if k >= 2 ** n:
            print(-1)
            return
        ans = ""
        #k -= 1
        for i in range(n):
            if k % 2:
                ans = ")" + ans
            else:
                ans = "(" + ans
            k >>= 1
        print(ans)
        return
    else:
        palList = [["()"]]
        while len(palList) < n // 2:
            tempList = set()
            for i in range((len(palList) + 1) // 2):
                for j in palList[i]:
                    for kk in palList[-i - 1]:
                        tempList.add(j + kk)
            for i in palList[-1]:
                tempList.add("(" + i + ")")
            palList.append(list(tempList))
        palSet = set(palList[-1])
        palList = []
        tempList = []
        allList = ["(", ")"]
        cnt = 1
        while cnt < n:
            temp = []
            for j in allList:
                temp.append(j + "(")
                temp.append(j + ")")
            allList = temp[:]
            cnt += 1
        allSet = set(allList)
        ansSet = allSet - palSet
        allSet = set()
        ansSet = list(ansSet)
        ansSet.sort()
        print(ansSet[k])
        return
        
    return

if __name__ == "__main__":
    main()