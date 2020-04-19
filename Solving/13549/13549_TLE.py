# Problem No.: 13549
# Solver:      Jinmin Goh
# Date:        20200417
# URL: https://www.acmicpc.net/problem/13549

import sys
sys.setrecursionlimit(10**8) 
ans = 0

def search(n: int, k: int, cnt: int) -> None:
    global ans
    if cnt >= ans:
        return
    #print(n, k, cnt, ans)
    if n >= k:
        ans = min(ans, cnt + n - k)
        return
    search(2 * n, k, cnt)
    search(n + 1, k, cnt + 1)
    search(n - 1, k, cnt + 1)


def main():
    n, k = map(int, input().split())
    if n >= k:
        print(n - k)
        return
    global ans
    ans = k - n
    search(n, k, 0)
    print(ans)
    return

if __name__ == "__main__":
    main()