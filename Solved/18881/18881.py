# Problem No.: 18881
# Solver:      Jinmin Goh
# Date:        20200709
# URL: https://www.acmicpc.net/problem/18881

import sys

def main():
    n = int(input())
    nums = []
    for _ in range(n):
        nums.append(list(map(int, sys.stdin.readline().split())))
    nums.sort()

    minRVal = 10 ** 7
    for i in range(n - 1):
        if nums[i][1] != nums[i + 1][1]:
            minRVal = min(nums[i + 1][0] - nums[i][0] - 1, minRVal)
    
    flag = False
    if nums[0][1] == 1:
        flag = True
    ans = 0
    for i in range(1, n):
        #print(nums[i], flag, ans)
        if nums[i][1] == 0:
            if flag:
                ans += 1
                flag = False
        else:
            if flag:
                if nums[i][0] - nums[i - 1][0] > minRVal:
                    ans += 1
            else:
                flag = True
    if flag:
        ans += 1
    print(ans)
    return

if __name__ == "__main__":
    main()