# Problem No.: 21394
# Solver:      Jinmin Goh
# Date:        20220627
# URL: https://www.acmicpc.net/problem/21394

import sys

def main():
    t = int(input())
    for _ in range(t):
        cnt_list = list(map(int, sys.stdin.readline().split()))
        cnt_list[8] += cnt_list[5]
        cnt_list[5] = 0
        temp = []
        for i in range(8, -1, -1):
            temp += [i + 1 for __ in range(cnt_list[i])]
        cnt = sum(cnt_list)
        ans = []
        if cnt % 2:
            for i in range(0, cnt, 2):
                ans.append(temp[i])
            for i in range(cnt - 2, -1, -2):
                ans.append(temp[i])
        else:
            for i in range(0, cnt, 2):
                ans.append(temp[i])
            for i in range(cnt - 1, -1, -2):
                ans.append(temp[i])
        for i in ans:
            print(i, end=" ")
        print()
    return

if __name__ == "__main__":
    main()