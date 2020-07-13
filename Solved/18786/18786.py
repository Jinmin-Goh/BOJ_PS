# Problem No.: 18786
# Solver:      Jinmin Goh
# Date:        20200713
# URL: https://www.acmicpc.net/problem/18786

import sys

def main():
    n = int(input())
    nums = []
    for _ in range(n):
        nums.append(tuple(map(int, input().split())))
    
    nums.sort()
    ans = 0
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if nums[i][0] == nums[j][0] and nums[j][1] == nums[k][1]:
                    #print("case1", nums[i], nums[j], nums[k])
                    ans = max(ans, abs((nums[i][1] - nums[j][1]) * (nums[j][0] - nums[k][0])))
                elif nums[i][1] == nums[j][1] and nums[j][0] == nums[k][0]:
                    #print("case2", nums[i], nums[j], nums[k])
                    ans = max(ans, abs((nums[i][0] - nums[j][0]) * (nums[j][1] - nums[k][1])))
                elif nums[i][0] == nums[k][0] and nums[j][1] == nums[k][1]:
                    #print("case3", nums[i], nums[j], nums[k])
                    ans = max(ans, abs((nums[i][1] - nums[k][1]) * (nums[j][0] - nums[k][0])))
                elif nums[i][1] == nums[k][1] and nums[j][0] == nums[k][0]:
                    #print("case4", nums[i], nums[j], nums[k])
                    ans = max(ans, abs((nums[i][0] - nums[k][0]) * (nums[j][1] - nums[k][1])))
                elif nums[i][0] == nums[j][0] and nums[i][1] == nums[k][1]:
                    #print("case5", nums[i], nums[j], nums[k])
                    ans = max(ans, abs((nums[i][1] - nums[j][1]) * (nums[i][0] - nums[k][0])))
                elif nums[i][1] == nums[j][1] and nums[i][0] == nums[k][0]:
                    #print("case6", nums[i], nums[j], nums[k])
                    ans = max(ans, abs((nums[i][0] - nums[j][0]) * (nums[i][1] - nums[k][1])))
                
    print(ans)

    return

if __name__ == "__main__":
    main()