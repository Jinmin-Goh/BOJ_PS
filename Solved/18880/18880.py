# Problem No.: 18880
# Solver:      Jinmin Goh
# Date:        20200708
# URL: https://www.acmicpc.net/problem/18880

import sys

def main():
    n = int(input())
    cowList = input()

    # no cow
    if "1" not in cowList:
        print(n - 1)
        return
    
    distance = []
    cnt = 1
    for i in range(n):
        if cowList[i] == "1":
            if i == 0:
                continue
            distance.append(cnt)
            cnt = 1
        else:
            cnt += 1
    if cowList[-1] != "1":
        distance.append(cnt)
    
    endList = []
    if cowList[0] == "0":
        endList.append(distance[0])
        distance = distance[1:]
    if cowList[-1] == "0":
        endList.append(distance.pop())
        
    distance.sort()
    if distance and distance[0] == 1:
        print(1)
        return
    endList.sort()
    #print(distance)
    #print(endList)
    
    tempAns = None
    if distance:
        tempAns = distance[-1] // 3

    temp = None
    if distance and distance[-1] != 1:
        temp = distance.pop()
    if temp == None:
        distance.append(endList.pop() - 1)
    elif endList and (temp // 2 + temp % 2 <= endList[-1] - 1):
        distance.append(temp)
        distance.append(endList.pop() - 1)
    else:
        distance += [temp // 2, temp // 2 + temp % 2]
    distance.sort()

    temp = None
    if distance[-1] != 1:
        temp = distance.pop()
    if temp == None:
        distance.append(endList.pop() - 1)
    elif endList and (temp // 2 + temp % 2 <= endList[-1] - 1):
        distance.append(temp)
        distance.append(endList.pop() - 1)
    else:
        distance += [temp // 2, temp // 2 + temp % 2]
    distance.sort()

    if tempAns:
        print(max(distance[0], tempAns))
    else:
        print(distance[0])


if __name__ == "__main__":
    main()