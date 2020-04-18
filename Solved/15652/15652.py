# Problem No.: 15652
# Solver:      Jinmin Goh
# Date:        20200417
# URL: https://www.acmicpc.net/problem/15652

import sys

def search(k: int, n: int, m: int, ans: [int]) -> None:
    if len(ans) == m:
        for i in ans:
            print(i, end = " ")
        print("")
        return
    for i in range(k, n + 1):
        ans.append(i)
        search(i, n, m, ans)
        ans.pop()
    return


def main():
    n, m = map(int, input().split())
    for i in range(n):
        search(i + 1, n, m, [i + 1])
    return

if __name__ == "__main__":
    main()