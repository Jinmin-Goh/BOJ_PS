# Problem No.: 2342
# Solver:      Jinmin Goh
# Date:        20220620
# URL: https://www.acmicpc.net/problem/2342

import sys

def main():
    nums = list(sys.stdin.readline().split())
    nums = [int(i) for i in nums]
    dp_table = [[[5000000, 5000000, 5000000, 5000000, 5000000] for _ in range(5)] for __ in range(len(nums))]
    dp_table[-1][0][0] = 0
    for i in range(len(nums) - 1):
        for j in range(5):
            for k in range(5):
                val = None
                if k == 0:
                    val = 2
                elif k == nums[i]:
                    val = 1
                elif abs(k - nums[i]) == 2:
                    val = 4
                else:
                    val = 3
                dp_table[i][nums[i]][j] = min(dp_table[i][nums[i]][j], dp_table[i - 1][k][j] + val)
                dp_table[i][j][nums[i]] = min(dp_table[i][j][nums[i]], dp_table[i - 1][j][k] + val)
            
                    
    minVal = 5000000
    for i in range(5):
        minVal = min(minVal, min(dp_table[-2][i]))
    print(minVal)
    return

if __name__ == "__main__":
    main()