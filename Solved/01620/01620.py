# Problem No.: 1620
# Solver:      Jinmin Goh
# Date:        20200410
# URL: https://www.acmicpc.net/problem/1620

import sys

def main():
    n, m = map(int, input().split())
    nameDict = {}
    numDict = {}
    for i in range(n):
        name = sys.stdin.readline().strip()
        nameDict[i + 1] = name
        numDict[name] = i + 1
    for i in range(m):
        query = sys.stdin.readline().strip()
        if query[0] in "1234567890":
            print(nameDict[int(query)])
        else:
            print(numDict[query])
    return

if __name__ == "__main__":
    main()