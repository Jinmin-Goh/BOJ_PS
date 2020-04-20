# Problem No.: 5639
# Solver:      Jinmin Goh
# Date:        20200421
# URL: https://www.acmicpc.net/problem/5639

import sys

sys.setrecursionlimit(10 ** 4 * 2)

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def postorder(head: TreeNode) -> None:
    if head.left:
        postorder(head.left)
    if head.right:
        postorder(head.right)
    print(head.val)

def main():
    temp = sys.stdin.readline().strip()
    head = TreeNode(int(temp))
    temp = sys.stdin.readline().strip()
    while temp:
        temp = int(temp)
        walker = head
        while True:
            if walker.left and temp < walker.val:
                walker = walker.left
            elif walker.right and temp > walker.val:
                walker = walker.right
            else:
                break
        temp = TreeNode(temp)
        if walker.val > temp.val:
            walker.left = temp
        if walker.val < temp.val:
            walker.right = temp
        temp = sys.stdin.readline().strip()
    postorder(head)
    return

if __name__ == "__main__":
    main()