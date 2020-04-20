# Problem No.: 5639
# Solver:      Jinmin Goh
# Date:        20200421
# URL: https://www.acmicpc.net/problem/5639

import sys

sys.setrecursionlimit(10 ** 4 * 2)

def postorder(nums: [int]) -> None:
    #print(nums)
    def binarySearch(pFront: int, pRear: int) -> None:
        #print("start:",pFront, pRear)
        if pFront > pRear:
            return
        head = nums[pFront]
        if pFront == pRear:
            print(head)
            return
        if head > nums[pRear] or head < nums[pFront + 1]:
            binarySearch(pFront + 1, pRear)
            print(head)
            return
        
        pFront += 1
        tempFront = pFront
        tempRear = pRear
        while tempFront + 1 < tempRear:
            tempMid = (tempFront + tempRear) // 2
            if nums[tempMid] > head:
                tempRear = tempMid
            else:
                tempFront = tempMid

        binarySearch(pFront, tempFront)
        binarySearch(tempFront + 1, pRear)
        print(head)

    binarySearch(0, len(nums) - 1)

def main():
    nums = []
    temp = sys.stdin.readline().strip()
    while temp:
        nums.append(int(temp))
        temp = sys.stdin.readline().strip()
    postorder(nums)
    return

if __name__ == "__main__":
    main()