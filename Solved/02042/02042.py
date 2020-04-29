# Problem No.: 2042
# Solver:      Jinmin Goh
# Date:        20200430
# URL: https://www.acmicpc.net/problem/2042

import sys

class SegTree():
    def __init__(self, nums: [int]):
        self.nums = nums
        cnt = 1
        while True:
            if cnt <= len(nums) < 2 * cnt:
                break
            cnt <<= 1
        self.treeList = [None] * cnt * 4
        
        def make(nodeIndex: int, start: int, end: int) -> int:
            # leaf node
            if start == end:
                self.treeList[nodeIndex] = nums[start]
                return self.treeList[nodeIndex]
            # other nodes
            else:
                self.treeList[nodeIndex] = make(nodeIndex * 2, start, (start + end) // 2) + make(nodeIndex * 2 + 1, (start + end) // 2 + 1, end)
                return self.treeList[nodeIndex]
        
        make(1, 0, len(nums) - 1)

    def update(self, location: int, n: int) -> None:
        diff = n - self.nums[location - 1]
        self.nums[location - 1] = n
        def newUpdate(nodeIndex: int, start: int, end: int) -> None:
            # if number is between the sum, update the node
            if start <= location <= end:
                self.treeList[nodeIndex] += diff
            else:
                return
            if start != end:
                newUpdate(nodeIndex * 2, start, (start + end) // 2)
                newUpdate(nodeIndex * 2 + 1, (start + end) // 2 + 1, end)
        newUpdate(1, 1, len(self.nums))

    def printSum(self, a: int, b: int) -> None:
        def newPrintSum(nodeIndex: int, start: int, end: int) -> int:
            if start > b or a > end:
                return 0
            elif start >= a and b >= end:
                return self.treeList[nodeIndex]
            else:
                return newPrintSum(2 * nodeIndex, start, (start + end) // 2) + newPrintSum(2 * nodeIndex + 1, (start + end) // 2 + 1, end)
        ans = newPrintSum(1, 1, len(self.nums))
        print(ans)

def main():
    n, m, k = map(int, input().split())
    nums = []
    for _ in range(n):
        nums.append(int(sys.stdin.readline().strip()))
    segTree = SegTree(nums)
    for _ in range(m + k):
        a, b, c = map(int, sys.stdin.readline().split())
        if a == 1:
            segTree.update(b, c)
        elif a == 2:
            segTree.printSum(b, c)
    return

if __name__ == "__main__":
    main()