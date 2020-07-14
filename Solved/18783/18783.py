# Problem No.: 18783
# Solver:      Jinmin Goh
# Date:        20200713
# URL: https://www.acmicpc.net/problem/18783

import sys

def main():
    n, m, k = map(int, input().split())
    nums = []
    for _ in range(m):
        nums.append(list(map(int, sys.stdin.readline().split())))
    
    change = [_ + 1 for _ in range(n)]
    #ans = [_ + 1 for _ in range(n)]
    
    # find final change result for single m-process
    for i in range(m):
        temp = list(reversed(change[nums[i][0] - 1:nums[i][1]]))
        change[nums[i][0] - 1:nums[i][1]] = temp
    #print(change)

    changeList = [None] * n     # list of changing sequences for each numbers
    cycleList = []      # list of cycles
    for i in range(n):
        if changeList[i] != None:
            continue
        # find cycle
        start = i + 1
        tempCycle = [start]
        temp = change[start - 1]
        #print(start, tempCycle, temp)
        while temp != start:
            tempCycle.append(temp)
            temp = change[temp - 1]
            #print(tempCycle)
        # add change list
        cycleList.append(tempCycle[:])
        for j in range(len(tempCycle)):
            changeList[tempCycle[j] - 1] = [j, len(cycleList) - 1]
    
    for i in range(n):
        print(cycleList[changeList[i][1]][(changeList[i][0] + k) % len(cycleList[changeList[i][1]])])
    
    return

if __name__ == "__main__":
    main()