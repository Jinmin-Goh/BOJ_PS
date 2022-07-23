# Problem No.: 5597
# Solver:      Jinmin Goh
# Date:        20220723
# URL: https://www.acmicpc.net/problem/5597

import sys

def main():
    nums = set([i + 1 for i in range(30)])
    for _ in range(28):
        nums.remove(int(input()))
    print(min(nums))
    print(max(nums))
    return

if __name__ == "__main__":
    main()