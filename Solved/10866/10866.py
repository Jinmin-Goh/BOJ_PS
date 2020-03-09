# Problem No.: 10866
# Solver:      Jinmin Goh
# Date:        20200309
# URL: https://www.acmicpc.net/problem/10866

import sys

def main():
    n = int(input())
    deque = []
    for i in range(n):
        order = sys.stdin.readline().split()
        if order[0] == "push_front":
            deque = [int(order[1])] + deque
        if order[0] == "push_back":
            deque.append(int(order[1]))
        if order[0] == "pop_front":
            if len(deque):
                print(deque.pop(0))
            else:
                print(-1)
        if order[0] == "pop_back":
            if len(deque):
                print(deque.pop())
            else:
                print(-1)
        if order[0] == "front":
            if len(deque):
                print(deque[0])
            else:
                print(-1)
        if order[0] == "back":
            if len(deque):
                print(deque[-1])
            else:
                print(-1)
        if order[0] == "size":
            print(len(deque))
        if order[0] == "empty":
            if len(deque):
                print(0)
            else:
                print(1)
        
    return

if __name__ == "__main__":
    main()