# Problem No.: 2675
# Solver:      Jinmin Goh
# Date:        20200308
# URL: https://www.acmicpc.net/problem/2675

import sys

def main():
    n = int(input())
    ans = []
    for i in range(n):
        temp = input().split()
        temp[0] = int(temp[0])
        tempStr = ""
        for j in temp[1]:
            tempStr += j * temp[0]
        ans.append(tempStr)
    for i in ans:
        print(i)
    return

if __name__ == "__main__":
    main()