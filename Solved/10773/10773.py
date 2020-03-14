# Problem No.: 10773
# Solver:      Jinmin Goh
# Date:        20200314
# URL: https://www.acmicpc.net/problem/10773

import sys

def main():
    n = int(input())
    stack = []
    for i in range(n):
        temp = int(sys.stdin.readline())
        if temp == 0:
            stack.pop()
        else:
            stack.append(temp)
    print(sum(stack))
    return

if __name__ == "__main__":
    main()