# Problem No.: 1016
# Solver:      Jinmin Goh
# Date:        20200320
# URL: https://www.acmicpc.net/problem/1016

import sys

def main():
    minVal, maxVal = map(int, input().split())
    nums = [True] * (10 ** 6 + 1)
    nums[0] = False
    nums[1] = False
    squareList = []
    for i in range(len(nums)):
        if nums[i]:
            squareList.append(i ** 2)
            temp = 2 * i
            while temp < len(nums):
                nums[temp] = False
                temp += i
    nums = [True for i in range(maxVal - minVal + 1)]
    for i in squareList:
        if i > maxVal:
            break
        temp = i - (minVal % i)
        if temp == i:
            temp = 0
        while temp < len(nums):
            nums[temp] = False
            temp += i

    print(sum(nums))

if __name__ == "__main__":
    main()