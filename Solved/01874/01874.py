# Problem No.: 1874
# Solver:      Jinmin Goh
# Date:        20200314
# URL: https://www.acmicpc.net/problem/1874

import sys

def main():
    n = int(input())
    nums = []
    for i in range(n):
        nums.append(int(sys.stdin.readline()))
    sequence = [n - i for i in range(n)]
    sequenceSet = set(sequence)
    stack = []
    stackSet = set()
    ans = ""
    for i in nums:
        if i in sequenceSet:
            while True:
                temp = sequence.pop()
                stack.append(temp)
                sequenceSet.remove(temp)
                stackSet.add(temp)
                ans += "+"
                if temp == i:
                    break
            temp = stack.pop()
            stackSet.remove(temp)
            ans += "-"
        elif i in stackSet:
            while True:
                if not stack or stack[-1] != i:
                    print("NO")
                    return
                temp = stack.pop()
                stackSet.remove(temp)
                ans += "-"
                if temp == i:
                    break
    for i in ans:
        print(i)

    return

if __name__ == "__main__":
    main()