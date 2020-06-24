# Problem No.: 16953
# Solver:      Jinmin Goh
# Date:        20200624
# URL: https://www.acmicpc.net/problem/16953

import sys

def main():
    n, k = map(int, input().split())
    
    flag = False
    ans = 1
    while k >= n:
        if n == k:
            flag = True
            break
        elif not k % 2:
            k //= 2
            ans += 1
        elif k % 10 == 1:
            k //= 10
            ans += 1
        else:
            break

    if flag:
        print(ans)
    else:
        print(-1)
    return

if __name__ == "__main__":
    main()