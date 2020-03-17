# Problem No.: 1259
# Solver:      Jinmin Goh
# Date:        20200317
# URL: https://www.acmicpc.net/problem/1259

import sys

def main():
    while True:
        string = sys.stdin.readline().split()
        string = string[0]
        if not string:
            print("yes")
            continue
        if string == "0":
            return
        flag = False
        for i in range(len(string) // 2):
            if string[i] != string[-i - 1]:
                flag = True
                break
        if flag:
            print("no")
        else:
            print("yes")

    return

if __name__ == "__main__":
    main()