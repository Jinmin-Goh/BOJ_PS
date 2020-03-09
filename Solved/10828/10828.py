# Problem No.: 10828
# Solver:      Jinmin Goh
# Date:        20200309
# URL: https://www.acmicpc.net/problem/10828

import sys

def main():
    n = int(input())
    stack = []
    for i in range(n):
        order = sys.stdin.readline().split()
        if order[0] == "push":
            stack.append(int(order[1]))
        if order[0] == "top":
            if len(stack):
                print(stack[-1])
            else:
                print(-1)
        if order[0] == "size":
            print(len(stack))
        if order[0] == "empty":
            if len(stack):
                print(0)
            else:
                print(1)
        if order[0] == "pop":
            if len(stack):
                print(stack.pop())
            else:
                print(-1)
    return

if __name__ == "__main__":
    main()