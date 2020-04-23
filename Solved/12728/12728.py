# Problem No.: 12728
# Solver:      Jinmin Goh
# Date:        20200423
# URL: https://www.acmicpc.net/problem/12728

import sys

# let a = 3 + 5^0.5, b = 3 - 5^0.5
# a + b = 6, ab = 4, a^2 + b^2 = 28
# a, b is a solution of equation x^2 - 6x + 4 = 0
# so, a^2 - 6a + 4 = b^2 - 6b + 4 = 0
# a^n = 6a^(n-1) 4a^(n-2) and same for b
# let p_n = a^n + b^n
# then, p_n = 6p_(n-1) - 4p_(n-2)
# b^n < 1 for positive integer n
# so if we know p_n, we can know integer part of a^n

# cycle length is 100, first 2 elements are not in cycle
# 
# [6, 28, 
#  144, 752, 936, 608, 904, 992, 336, 48, 944, 472,
#  56, 448, 464, 992, 96, 608, 264, 152, 856, 528,
#  744, 352, 136, 408, 904, 792, 136, 648, 344, 472,
#  456, 848, 264, 192, 96, 808, 464, 552, 456, 528,
#  344, 952, 336, 208, 904, 592, 936, 248, 744, 472,
#  856, 248, 64, 392, 96, 8, 664, 952, 56, 528,
#  944, 552, 536, 8, 904, 392, 736, 848, 144, 472,
#  256, 648, 864, 592, 96, 208, 864, 352, 656, 528,
#  544, 152, 736, 808, 904, 192, 536, 448, 544, 472,
#  656, 48, 664, 792, 96, 408, 64, 752, 256, 528]

def main():
    nums = [6, 28]
    numSet = set(nums)
    temp = 6 * nums[-1] - 4 * nums[-2]
    
    for _ in range(100):
        nums.append(temp)
        numSet.add(temp)
        temp = (6 * nums[-1] - 4 * nums[-2]) % 1000
    cycleList = nums[2:]
    t = int(input())
    for _ in range(t):
        n = int(sys.stdin.readline().strip())
        ans = None
        if n <= 2:
            ans = str(nums[n - 1] - 1)
        else:
            ans = str(cycleList[(n - 2) % len(cycleList) - 1] - 1)
        while len(ans) < 3:
            ans = "0" + ans
        ans = "Case #" + str(_ + 1) + ": " + ans
        print(ans)

    return

if __name__ == "__main__":
    main()