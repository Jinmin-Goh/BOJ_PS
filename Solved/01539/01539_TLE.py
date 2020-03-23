# Problem No.: 1539
# Solver:      Jinmin Goh
# Date:        20200323
# URL: https://www.acmicpc.net/problem/1539

import sys

# implemented BST, TLE in 12%
# worst case(O(n^2)) is problem

class TreeNode:
    def __init__(self, x: int):
        self.val = x
        self.right = None
        self.left = None

def main():
    n = int(input())
    head = None
    ans = 0
    nums = []
    for _ in range(n):
        x = int(sys.stdin.readline())
        nums.append(x)
    temp = nums[:]
    temp.sort()
    revTemp = list(reversed(temp))
    #print(temp, nums, revTemp)
    if temp == nums or revTemp == nums:
        print(n * (n + 1) // 2)
        return
    for x in nums:
        if not head:
            head = TreeNode(x)
            ans += 1
            continue
        cnt = 1
        walker = head
        while True:
            if not(walker.left or walker.right):
                break
            if x < walker.val:
                if not walker.left:
                    break
                walker = walker.left
            else:
                if not walker.right:
                    break
                walker = walker.right
            cnt += 1
        if x < walker.val:
            walker.left = TreeNode(x)
        else:
            walker.right = TreeNode(x)
        cnt += 1
        ans += cnt
    print(ans)
    return

if __name__ == "__main__":
    main()