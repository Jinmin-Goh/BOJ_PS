# Problem No.: 15654
# Solver:      Jinmin Goh
# Date:        20200413
# URL: https://www.acmicpc.net/problem/15654

import sys

def main():
    n, m = map(int, input().split())
    nums = list(map(int, sys.stdin.readline().split()))
    nums.sort()
    if m == 1:
        for i in range(n):
            print(nums[i])
        return
    temp = nums[:m]
    tempIndex = [_ for _ in range(m)]
    end = list(reversed(nums[-m:]))
    #endIndex = [_ for _ in reversed(range(n - m, n - 1))]

    numSet = set([_ for _ in range(m, n)])
    usedSet = set()
    for i in temp:
        print(i, end = " ")
    print("")
    while temp != end:
        pos = -1
        if not numSet:
            usedSet.add(tempIndex[pos])
            tempIndex[pos] = None
            pos -= 1
            while tempIndex[pos] > max(usedSet):
                usedSet.add(tempIndex[pos])
                tempIndex[pos] = None
                pos -= 1
            numSet = set(list(usedSet))
            usedSet = set()
            numSet.add(tempIndex[pos])
            #print(numSet, usedSet, pos, tempIndex[pos])
            tempIndex[pos] += 1
            while tempIndex[pos] not in numSet:
                tempIndex[pos] += 1
            temp[pos] = nums[tempIndex[pos]]
            numSet.remove(tempIndex[pos])
            #print(numSet, usedSet)
            pos += 1
            while pos < 0:
                tempIndex[pos] = min(numSet)
                temp[pos] = nums[tempIndex[pos]]
                numSet.remove(tempIndex[pos])
                pos += 1
            #print(numSet, usedSet)
            
        else:
            usedSet.add(tempIndex[pos])
            tempIndex[pos] = min(numSet)
            temp[pos] = nums[tempIndex[pos]]
            numSet.remove(tempIndex[pos])
        for i in temp:
            print(i, end = " ")
        print("")

    return

if __name__ == "__main__":
    main()