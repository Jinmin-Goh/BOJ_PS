# Problem No.: 1107
# Solver:      Jinmin Goh
# Date:        20200623
# URL: https://www.acmicpc.net/problem/1107

import sys

def main():
    n = int(input())
    m = int(input())
    if m != 0:
        broken = list(input().split())
    
    nLen = len(str(n))
    if m == 0:
        print(min(nLen, abs(n - 100)))
        return
    if m == 10:
        print(abs(100 - n))
        return
    
    notbroken = []
    temp = "0123456789"
    for i in temp:
        if i not in broken:
            notbroken.append(i)
    
    if notbroken == ["0"]:
        print(min(abs(100 - n), 1 + n))
        return
    
    candidate = notbroken[:]
    cnt = 1
    while cnt < nLen:
        cnt += 1
        temp = candidate[:]
        candidate = []
        for i in notbroken:
            for j in temp:
                candidate.append(j + i)

    tempMin = notbroken[-1] * (nLen - 1)
    if "0" in notbroken:
        tempMax = notbroken[1] + "0" * nLen
    else:
        tempMax = notbroken[0] * (nLen + 1)
    
    if nLen > 1:
        candidate += [tempMax, tempMin]
    else:
        candidate += [tempMax]
    
    ans = 500000
    for i in candidate:
        temp = int(i)
        ans = min(ans, len(str(temp)) + abs(temp - n))
    ans = min(ans, abs(n - 100))
    print(ans)
    return

if __name__ == "__main__":
    main()