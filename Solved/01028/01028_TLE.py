# Problem No.: 1028
# Solver:      Jinmin Goh
# Date:        20200326
# URL: https://www.acmicpc.net/problem/1028

import sys

def main():
    R, C = map(int, input().split())
    mapTable = []
    sumVal = 0
    for _ in range(R):
        temp = input()
        tempList = []
        for i in temp:
            tempList.append(int(i))
        mapTable.append(tempList)
        sumVal += sum(mapTable[-1])
    if sumVal == 0:
        print(0)
        return
    maxSize = (min(R, C) + 1) // 2
    ans = 1
    for i in range(R):
        for j in range(C):
            flag = True
            tempAns = ans
            for k in range(ans + 1, maxSize + 1):
                flag = True
                for s in range(k - 1):
                    # left down
                    if i - (k - 1) + s < 0 or i - (k - 1) + s >= R or j - s < 0 or j - s >= C:
                        flag = False
                        break
                    if mapTable[i - (k - 1) + s][j - s] == 0:
                        flag = False
                        break
                    # right down
                    if i + s < 0 or i + s >= R or j - (k - 1) + s < 0 or j - (k - 1) + s >= C:
                        flag = False
                        break
                    if mapTable[i + s][j - (k - 1) + s] == 0:
                        flag = False
                        break
                    # right up
                    if i + (k - 1) - s < 0 or i + (k - 1) - s >= R or j + s < 0 or j + s >= C:
                        flag = False
                        break
                    if mapTable[i + (k - 1) - s][j + s] == 0:
                        flag = False
                        break
                    # left up
                    if i - s < 0 or i - s >= R or j + (k - 1) - s < 0 or j + (k - 1) - s >= C:
                        flag = False
                        break
                    if mapTable[i - s][j + (k - 1) - s] == 0:
                        flag = False
                        break
                    #print("test", i, j, k, s)
                if flag:
                    tempAns = max(ans, k)
            ans = tempAns 
    print(ans)
    return

if __name__ == "__main__":
    main()