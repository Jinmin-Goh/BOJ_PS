# Problem No.: 5582
# Solver:      Jinmin Goh
# Date:        20200317
# URL: https://www.acmicpc.net/problem/5582

import sys

def main():
    s = input()
    t = input()
    ans = 0
    i , j = 0, 0
    for i in range(len(s)):
        sameFlag = False
        cnt = 0
        tempI = i
        for j in range(len(t)):
            if tempI >= len(s):
                ans = max(cnt, ans)
                break
            #print(i, tempI, j, s[tempI], t[j], sameFlag, cnt, ans)
            if s[tempI] == t[j]:
                if not sameFlag:
                    sameFlag = True
                cnt += 1
                tempI += 1
            else:
                if sameFlag:
                    ans = max(cnt, ans)
                    sameFlag = False
                    cnt = 0
                tempI = i
    s, t = t, s
    i , j = 0, 0
    for i in range(len(s)):
        sameFlag = False
        cnt = 0
        tempI = i
        for j in range(len(t)):
            if tempI >= len(s):
                ans = max(cnt, ans)
                break
            #print(i, tempI, j, s[tempI], t[j], sameFlag, cnt, ans)
            if s[tempI] == t[j]:
                if not sameFlag:
                    sameFlag = True
                cnt += 1
                tempI += 1
            else:
                if sameFlag:
                    ans = max(cnt, ans)
                    sameFlag = False
                    cnt = 0
                tempI = i
    print(ans)
    return

if __name__ == "__main__":
    main()