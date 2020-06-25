# Problem No.: 12851
# Solver:      Jinmin Goh
# Date:        20200625
# URL: https://www.acmicpc.net/problem/12851

import sys
import collections

def main():
    n, k = map(int, input().split())
    
    time = [None] * (10 ** 5 + 1)

    stack = collections.deque([n])
    
    ans = [0, 0]
    cnt = 0
    while True:
        stack.append(None)
        while stack:
            temp = stack.popleft()
            if temp == None:
                break
            if time[temp] != None and temp == k:
                ans[1] += 1
                ans[0] = cnt
            if time[temp] != None and time[temp][0] < cnt:
                continue
            elif time[temp]:
                time[temp][1] += 1
            else:
                time[temp] = [cnt, 1]
            
    
            if temp > 0 and (time[temp - 1] == None or time[temp - 1][0] == cnt):
                stack.append(temp - 1)
            if temp < 10 ** 5 and (time[temp + 1] == None or time[temp + 1][0] == cnt):
                stack.append(temp + 1)
            if 2 * temp <= 10 ** 5 and (time[temp * 2] == None or time[temp * 2][0] == cnt):
                stack.append(temp * 2)
    
        cnt += 1
        if time[k] != None:
            break

    print(time[k][0])
    print(time[k][1])
    return

if __name__ == "__main__":
    main()