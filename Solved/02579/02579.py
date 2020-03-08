# Problem No.: 2579
# Solver:      Jinmin Goh
# Date:        20200308
# URL: https://www.acmicpc.net/problem/2579

import sys

def main():
    n = int(input())
    score = []
    for i in range(n):
        score.append(int(input()))
    if n <= 2:
        print(sum(score))
        return
    elif n == 3:
        print(sum(score) - min(score[:n - 1]))
        return
    dpList = [-1] * n
    dpList[0] = score[0]
    dpList[1] = sum(score[:2])
    dpList[2] = sum(score[:3]) - min(score[:2])
    for i in range(3, n):
        dpList[i] = max(dpList[i - 2] + score[i], dpList[i - 3] + score[i] + score[i - 1])
    print(dpList[-1])

if __name__ == "__main__":
    main()