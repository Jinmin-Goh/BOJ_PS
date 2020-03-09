# Problem No.: 4153
# Solver:      Jinmin Goh
# Date:        20200309
# URL: https://www.acmicpc.net/problem/4153

import sys

def main():
    ans = []
    while True:
        temp = input().split()
        if temp == ["0", "0", "0"]:
            break
        temp = [int(_) for _ in temp]
        temp.sort()
        if temp[-1] ** 2 == temp[0] ** 2 + temp[1] ** 2:
            ans.append("right")
        else:
            ans.append("wrong")
    for i in ans:
        print(i)
    return

if __name__ == "__main__":
    main()