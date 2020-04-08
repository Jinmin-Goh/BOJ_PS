# Problem No.: 7662
# Solver:      Jinmin Goh
# Date:        20200317
# URL: https://www.acmicpc.net/problem/7662

import sys

def main():
    T = int(input())
    for i in range(T):
        n = int(sys.stdin.readline())
        stackDict = {}
        for j in range(n):
            temp = sys.stdin.readline().split()
            order = temp[0]
            num = int(temp[1])
            if order == "I":
                if num not in stackDict:
                    stackDict[num] = 1
                else:
                    stackDict[num] += 1
            elif num == 1:
                if not stackDict:
                    continue
                maxVal = max(stackDict)
                stackDict[maxVal] -= 1
                if stackDict[maxVal] == 0:
                    del stackDict[maxVal]
            else:
                if not stackDict:
                    continue
                minVal = min(stackDict)
                stackDict[minVal] -= 1
                if stackDict[minVal] == 0:
                    del stackDict[minVal]
        if not stackDict:
            print("EMPTY")
        else:
            print(max(stackDict), min(stackDict))
    return

if __name__ == "__main__":
    main()