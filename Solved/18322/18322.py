# Problem No.: 18322
# Solver:      Jinmin Goh
# Date:        20200710
# URL: https://www.acmicpc.net/problem/18322

import sys

def main():
    n, k = map(int, input().split())
    words = sys.stdin.readline().split()
    words = list(reversed(words))
    cnt = 0
    ans = ""
    while words:
        temp = words.pop()
        if cnt + len(temp) > k:
            print(ans[:-1])
            cnt = 0
            ans = ""
        cnt += len(temp)
        ans += temp + " "
    if ans:
        print(ans[:-1])
    return

if __name__ == "__main__":
    main()