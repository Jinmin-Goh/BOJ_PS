# Problem No.: 02565
# Solver:      Jinmin Goh
# Date:        20220630
# URL: https://www.acmicpc.net/problem/02565

import sys

def main():
    n = int(input())
    lines = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
    lines.sort()
    # find LIS
    nums = [i for (_, i) in lines]
    dp = []
    for i in range(n):
        if not dp:
            dp.append([nums[i]])
            continue
        if len(dp) == 1:
            if dp[0][-1] >= nums[i]:
                dp[0].append(nums[i])
            else:
                dp.append([nums[i]])
        else:
            pFront = 0
            pRear = len(dp) - 1
            while pFront < pRear < len(dp):
                pMid = (pFront + pRear) // 2
                if dp[pMid][-1] < nums[i]:
                    pFront = pMid + 1
                else:
                    pRear = pMid
            if pFront >= len(dp) - 1:
                if dp[-1][-1] >= nums[i]:
                    dp[-1].append(nums[i])
                else:
                    dp.append([nums[i]])
            else:
                dp[pFront].append(nums[i])
    LIS = []
    for i in reversed(range(len(dp))):
        if not LIS:
            LIS.append(dp[i][0])
        else:
            for j in dp[i]:
                if LIS[-1] > j:
                    LIS.append(j)
                    break
    print(n - len(LIS))
    return

if __name__ == "__main__":
    main()