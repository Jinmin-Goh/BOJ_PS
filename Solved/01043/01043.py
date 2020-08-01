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
        partyList[-1].pop(0)
    
    if trueList[0] == 0:
        print(m)
        return
    trueList.pop(0)
    trueSet = set(trueList)
    for _ in range(51):
        for i in range(m):
            flag = False
            for j in partyList[i]:
                if j in trueSet:
                    flag = True
                    break
            if flag:
                for j in partyList[i]:
                    trueSet.add(j)

    ans = 0
    for i in range(m):
        flag = False
        for j in partyList[i]:
            if j in trueSet:
                flag = True
                break
        if not flag:
            ans += 1
    print(ans)
    
    return

if __name__ == "__main__":
    main()