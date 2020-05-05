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
        def dp(pos: int, upFlag: bool) -> int:
            if pos == n - 2:
                return max(nums[upFlag][pos] + nums[not upFlag][pos + 1], nums[upFlag][pos + 1])
            elif pos == n - 1:
                return nums[upFlag][-1]
            ans = 0
            while pos < n:
                if pos < n - 2:
                    ans += nums[upFlag][pos]
                    if nums[not upFlag][pos + 1] + nums[upFlag][pos + 2] > nums[not upFlag][pos + 2]:
                        pos += 1
                        upFlag = not upFlag
                    elif nums[not upFlag][pos + 1] + nums[upFlag][pos + 2] < nums[not upFlag][pos + 2]:
                        pos += 2
                        upFlag = not upFlag
                    else:
                        ans += max(dp(pos + 1, not upFlag), dp(pos + 2, not upFlag))
                        break
                else:
                    ans += dp(pos, upFlag)
                    break
            return ans
        
        print(max(dp(0, True), dp(0, False)))
    return

if __name__ == "__main__":
    main()