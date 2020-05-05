# Problem No.: 9465
# Solver:      Jinmin Goh
# Date:        20200506
# URL: https://www.acmicpc.net/problem/9465

import sys

def main():
    t = int(input())
    for _ in range(t):
        n = int(sys.stdin.readline().strip())
        nums = []
        nums.append(list(map(int, sys.stdin.readline().split())))
        nums.append(list(map(int, sys.stdin.readline().split())))
        dpList = [[0] * (n + 1) for _ in range(3)]
        for i in range(1, n + 1):
            dpList[0][i] = max(dpList[1][i - 1], dpList[2][i - 1]) + nums[0][i - 1]
            dpList[1][i] = max(dpList[0][i - 1], dpList[2][i - 1]) + nums[1][i - 1]
            dpList[2][i] = max(dpList[1][i - 1], dpList[0][i - 1])
        print(max(dpList[0][-1], dpList[1][-1], dpList[2][-1]))
        
    return

if __name__ == "__main__":
    main()