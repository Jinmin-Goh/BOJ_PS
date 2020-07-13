# Problem No.: 18787
# Solver:      Jinmin Goh
# Date:        20200713
# URL: https://www.acmicpc.net/problem/18787

import sys

def main():
    # parsing
    n = int(input())
    strA = input()
    strB = input()

    diffFlag = False
    ans = 0
    pointer = 0
    while pointer < n:
        if strA[pointer] == strB[pointer]:
            if diffFlag:
                diffFlag = False
        else:
            if not diffFlag:
                diffFlag = True
                ans += 1
        pointer += 1
    print(ans)
    return

if __name__ == "__main__":
    main()