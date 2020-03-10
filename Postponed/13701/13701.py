# Problem No.: 13701
# Solver:      Jinmin Goh
# Date:        20200310
# URL: https://www.acmicpc.net/problem/13701

import sys

def main():
    nums = input().split()
    numSet = set()
    while True:
        if len(nums) == 0:
            break
        temp = nums.pop(0)
        if temp not in numSet:
            numSet.add(temp)
            print(temp, end=" ")        
    return

if __name__ == "__main__":
    main()