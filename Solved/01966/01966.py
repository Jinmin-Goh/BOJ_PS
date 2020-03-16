# Problem No.: 1966
# Solver:      Jinmin Goh
# Date:        20200316
# URL: https://www.acmicpc.net/problem/1966

import sys

def main():
    T = int(input())
    for i in range(T):
        n, m = map(int, sys.stdin.readline().split())
        stack = list(map(int, sys.stdin.readline().split()))
        priorityDict = {}
        for i in range(len(stack)):
            if stack[i] not in priorityDict:
                priorityDict[stack[i]] = 1
            else:
                priorityDict[stack[i]] += 1
            stack[i] = [stack[i], i]
        targetPriority = stack[m][0]
        maxPriority = max(priorityDict)
        #print(stack, targetPriority, maxPriority, priorityDict)
        cnt = 0
        while maxPriority >= targetPriority:
            if stack[0][0] == maxPriority:
                priorityDict[stack[0][0]] -= 1
                if priorityDict[stack[0][0]] == 0:
                    del priorityDict[stack[0][0]]
                    if priorityDict:
                        maxPriority = max(priorityDict)
                    else:
                        maxPriority = -1
                temp = stack.pop(0)
                #print(temp)
                cnt += 1
                if temp == [targetPriority, m]:
                    break
            if stack[0][0] < maxPriority:
                stack.append(stack.pop(0))
        print(cnt)            
    return

if __name__ == "__main__":
    main()