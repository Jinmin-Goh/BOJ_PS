# Problem No.: 1490
# Solver:      Jinmin Goh
# Date:        20220905
# URL: https://www.acmicpc.net/problem/1490

import sys

def main():
    n = sys.stdin.readline().rstrip()
    nums = [int(i) for i in n]
    nums = list(set(nums))
    ans = int(n)
    flag = True
    for j in nums:
        if j == 0:
            continue
        if ans % j:
            flag = False
    if flag:
        print(ans)
        return
    for l in range(7):
        for i in range(10 ** l):
            temp = int(n + '0' * (l - len(str(i))) + str(i))
            flag = True
            for j in nums:
                if j == 0:
                    continue
                if temp % j:
                    flag = False
            if flag:
                print(temp)
                return
    return

if __name__ == "__main__":
    main()