# Problem No.: 9250
# Solver:      Jinmin Goh
# Date:        20200317
# URL: https://www.acmicpc.net/problem/9250

import sys

def main():
    s1 = input()
    s2 = input()
    if len(s1) == 0 or len(s2) == 0:
        print(0)
        print("")
        return
    dpList = [[0] * (len(s2) + 1) for i in range(len(s1) + 1)]
    maxVal = 0
    ans = ""
    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            #print(i, j)
            if s1[i - 1] == s2[j - 1]:
                dpList[i][j] = dpList[i - 1][j - 1] + 1
                if maxVal < dpList[i][j]:
                    maxVal = dpList[i][j]
            else:
                dpList[i][j] = max(dpList[i - 1][j], dpList[i][j - 1])
    #print(dpList)
    tempCnt = maxVal
    for i in reversed(range(1, len(s1) + 1)):
        for j in reversed(range(1, len(s2) + 1)):
            if dpList[i][j] == tempCnt and s1[i - 1] == s2[j - 1]:
                ans = s1[i - 1] + ans
                tempCnt -= 1
                break
    print(maxVal)
    print(ans)
    return

if __name__ == "__main__":
    main()