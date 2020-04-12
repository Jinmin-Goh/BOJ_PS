# Problem No.: 15650
# Solver:      Jinmin Goh
# Date:        20200413
# URL: https://www.acmicpc.net/problem/15650

import sys

def main():
    n, m = map(int, input().split())
    if m == 1:
        for i in range(n):
            print(i + 1)
    elif m == n:
        for i in range(n):
            print(i + 1, end = " ")
    else:
        temp = [_ + 1 for _ in range(m)]
        for i in temp:
            print(i, end = " ")
        print("")
        end = [_ + 1 + n - m for _ in range(m)]
        while temp != end:
            pos = -1
            if temp[pos] == n:
                pos -= 1
                while True:
                    if temp[pos] == n + pos + 1:
                        pos -= 1
                    else:
                        temp[pos] += 1
                        break
                #print(pos, temp)
                while pos < -1:
                    temp[pos + 1] = temp[pos] + 1
                    pos += 1
                #print(pos, temp)
            else:
                temp[pos] += 1
            for i in temp:
                print(i, end = " ")
            print("")
    return

if __name__ == "__main__":
    main()