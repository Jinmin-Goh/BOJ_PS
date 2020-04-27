# Problem No.: 10993
# Solver:      Jinmin Goh
# Date:        20200428
# URL: https://www.acmicpc.net/problem/10993

import sys

def main():
    n = int(input())
    ans = ["*"]
    cnt = 1
    upFlag = True
    while cnt < n:
        upFlag = not upFlag
        temp = []
        for i in range(len(ans) * 2 + 1):
            if upFlag:
                if i == 0:
                    temp.append(" " * (len(ans) * 2 - i) + "*" + " " * (len(ans) * 2 - i))
                elif i == len(ans) * 2:
                    temp.append("*" * (len(ans) * 4 + 1))
                elif len(ans) <= i < len(ans) * 2:
                    temp.append(" " * (len(ans) * 2 - i) + "*" + " " * (i - len(ans)) + ans[i - len(ans)] + " " *(i - len(ans)) + "*" + " " * (len(ans) * 2 - i))
                else:
                    temp.append(" " * (len(ans) * 2 - i) + "*" + " " * (2 * i - 1) + "*" + " " * (len(ans) * 2 - i))

            else:
                if i == 0:
                    temp.append("*" * (len(ans) * 4 + 1))
                elif i == len(ans) * 2:
                    temp.append(" " * i + "*" + " " * i)
                elif i <= len(ans):
                    temp.append(" " * i + "*" + " " * (len(ans) - i) + ans[i - 1] + " " * (len(ans) - i) + "*" + " " * i)
                else:
                    temp.append(" " * i + "*" + " " * (len(ans) * 4 - 2 * i - 1) + "*" + " " * i)
        ans = temp[:]
        cnt += 1
    for i in ans:
        print(i.rstrip())
    return

if __name__ == "__main__":
    main()