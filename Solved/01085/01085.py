# Problem No.: 1085
# Solver:      Jinmin Goh
# Date:        20200309
# URL: https://www.acmicpc.net/problem/1085

import sys

def main():
    nums = input().split()
    nums = [int(_) for _ in nums]
    print(min(nums[0], nums[1], nums[2] - nums[0], nums[3] - nums[1]))
    return

if __name__ == "__main__":
    main()