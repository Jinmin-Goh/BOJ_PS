# Problem No.: 19288
# Solver:      Jinmin Goh
# Date:        20220629
# URL: https://www.acmicpc.net/problem/19288

# solution from https://codeforces.com/blog/entry/57694

import sys

def main():
    n, k = map(int, sys.stdin.readline().split())
    curr = list(map(int, sys.stdin.readline().split()))
    curr = [(i, k) for i in curr]
    next = []
    while True:
        sum_val = 0
        for i, cnt in curr:
            if cnt != 0:
                sum_val += 3 ** cnt
        curr_sort = curr[:]
        curr_sort.sort()
        ans = None
        half_val = 0
        for i, cnt in curr_sort:
            if cnt != 0:
                half_val += 3 ** cnt
            if sum_val // 2 <= half_val:
                ans = i
                break
        print(ans)
        sys.stdout.flush()
        r = sys.stdin.readline().rstrip()
        if r == "End":
            break
        elif r == "<=":
            next = list(map(int, sys.stdin.readline().split()))
            for i in range(n):
                if ans >= curr[i][0] and curr[i][0] != 0:
                    next[i] = (next[i], curr[i][1] - 1)
                else:
                    next[i] = (next[i], curr[i][1])
        elif r == ">=":
            next = list(map(int, sys.stdin.readline().split()))
            for i in range(n):
                if ans <= curr[i][0] and curr[i][0] != 0:
                    next[i] = (next[i], curr[i][1] - 1)
                else:
                    next[i] = (next[i], curr[i][1])
        curr = next
        
    return

if __name__ == "__main__":
    main()