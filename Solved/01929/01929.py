# Problem No.: 1929
# Solver:      Jinmin Goh
# Date:        20200314
# URL: https://www.acmicpc.net/problem/1929

import sys

def main():
    m, n = map(int, input().split())
    nList = [True for i in range(n + 1)]
    nList[0] = False
    nList[1] = False
    primeList = []
    for i in range(2, n + 1):
        if nList[i]:
            temp = 2 * i
            while temp <= n:
                nList[temp] = False
                temp += i
            primeList.append(i)
    #print(primeList)
    #print(ansList)
    for i in range(m, n + 1):
        if nList[i]:
            print(i, end = " ")
    return

if __name__ == "__main__":
    main()