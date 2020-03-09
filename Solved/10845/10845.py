# Problem No.: 10845
# Solver:      Jinmin Goh
# Date:        20200309
# URL: https://www.acmicpc.net/problem/10845

import sys

def main():
    n = int(input())
    queue = []
    for i in range(n):
        order = sys.stdin.readline().split()
        if order[0] == "push":
            queue.append(int(order[1]))
        if order[0] == "front":
            if len(queue):
                print(queue[0])
            else:
                print(-1)
        if order[0] == "back":
            if len(queue):
                print(queue[-1])
            else:
                print(-1)
        if order[0] == "size":
            print(len(queue))
        if order[0] == "empty":
            if len(queue):
                print(0)
            else:
                print(1)
        if order[0] == "pop":
            if len(queue):
                print(queue.pop(0))
            else:
                print(-1)
    return

if __name__ == "__main__":
    main()