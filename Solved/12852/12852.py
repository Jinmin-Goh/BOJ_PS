# Problem No.: 12852
# Solver:      Jinmin Goh
# Date:        20220614
# URL: https://www.acmicpc.net/problem/12852

import sys

def main():
    n = int(input())
    dpList = [10 ** 7 for _ in range(10 ** 6 + 1)]
    dpList[1] = 0
    for i in range(2, 10 ** 6 + 1):
        if not (i % 3):
            dpList[i] = min(dpList[i], dpList[i // 3] + 1)
        if not (i % 2):
            dpList[i] = min(dpList[i], dpList[i // 2] + 1)
        dpList[i] = min(dpList[i], dpList[i - 1] + 1)
    print(dpList[n])
    ans = [n]
    temp = n
    while temp > 1:
        flag2 = False
        flag3 = False
        if not (temp % 3):
            flag3 = True
        if not (temp % 2):
            flag2 = True
        if flag3 and flag2:
            if min(dpList[temp // 3], dpList[temp // 2], dpList[temp - 1]) == dpList[temp // 3]:
                ans.append(temp // 3)
                temp //= 3
            elif min(dpList[temp // 3], dpList[temp // 2], dpList[temp - 1]) == dpList[temp // 2]:
                ans.append(temp // 2)
                temp //= 2
            else:
                ans.append(temp - 1)
                temp -= 1
        elif flag2:
            if min(dpList[temp // 2], dpList[temp - 1]) == dpList[temp // 2]:
                ans.append(temp // 2)
                temp //= 2
            else:
                ans.append(temp - 1)
                temp -= 1
        elif flag3:
            if min(dpList[temp // 3], dpList[temp - 1]) == dpList[temp // 3]:
                ans.append(temp // 3)
                temp //= 3
            else:
                ans.append(temp - 1)
                temp -= 1
        else:
            ans.append(temp - 1)
            temp -= 1
        
    for i in ans:
        print(i, end=" ")
    return

if __name__ == "__main__":
    main()