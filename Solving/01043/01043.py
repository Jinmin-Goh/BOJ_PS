# Problem No.: 1043
# Solver:      Jinmin Goh
# Date:        20200704
# URL: https://www.acmicpc.net/problem/1043

import sys

def main():
    n, m = map(int, input().split())
    trueList = list(map(int, sys.stdin.readline().split()))
    partyList = []
    for _ in range(m):
        partyList.append(list(map(int, sys.stdin.readline().split())))
    
    if trueList[0] == 0:
        print(m)
        return
    
    
    return

if __name__ == "__main__":
    main()