# Problem No.: 16287
# Solver:      Jinmin Goh
# Date:        20220722
# URL: https://www.acmicpc.net/problem/16287

import sys

def main():
    w, n = map(int, sys.stdin.readline().split())
    nums = list(map(int, sys.stdin.readline().split()))
    nums_dict = {}
    for i in range(n - 1):
        for j in range(i + 1, n):
            val = nums[i] + nums[j]
            if val not in nums_dict:
                nums_dict[val] = []
                nums_dict[val].append((i, j))
    for i in range(n - 1):
        for j in range(i + 1, n):
            val = nums[i] + nums[j]
            if w - val in nums_dict:
                for pair in nums_dict[w - val]:
                    if i not in pair and j not in pair:
                        print('YES')
                        return
    
    print('NO')
    return

if __name__ == "__main__":
    main()