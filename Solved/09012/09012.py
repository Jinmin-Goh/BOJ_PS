# Problem No.: 9012
# Solver:      Jinmin Goh
# Date:        20200309
# URL: https://www.acmicpc.net/problem/9012

import sys

def main():
    n = int(input())
    ans = []
    for i in range(n):
        word = input()
        cnt = 0
        flag = False
        for i in word:
            if i == "(":
                cnt += 1
            else:
                if cnt == 0:
                    ans.append("NO")
                    flag = True
                    break
                else:
                    cnt -= 1
        if flag:
            continue
        if cnt != 0:
            ans.append("NO")
        else:
            ans.append("YES")
    for i in ans:
        print(i)
    return

if __name__ == "__main__":
    main()