# Problem No.: 2448
# Solver:      Jinmin Goh
# Date:        20200423
# URL: https://www.acmicpc.net/problem/2448

import sys

def main():
    n = int(input())
    n = n // 3
    
    ans = ["  *  ",
           " * * ",
           "*****"]
    while n > 1:
        n >>= 1
        temp = []
        for i in ans:
            temp.append(" " * len(ans) + i + " " * len(ans))
        for i in ans:
            temp.append(i + " " + i)
        ans = temp[:]
    for i in ans:
        print(i)

    return

if __name__ == "__main__":
    main()