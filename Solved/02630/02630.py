# Problem No.: 2630
# Solver:      Jinmin Goh
# Date:        20200411
# URL: https://www.acmicpc.net/problem/2630

import sys

def main():
    n = int(input())
    nums = []
    for _ in range(n):
        nums.append(list(map(int, sys.stdin.readline().split())))
    
    def check(x: int, y: int, length: int) -> [int]:
        if length == 1:
            if nums[x][y] == 0:
                return [1, 0]
            else:
                return [0, 1]
        num = nums[x][y]
        flag = True
        for i in range(length):
            for j in range(length):
                if nums[x + i][y + j] != num:
                    flag = False
                    break
            if not flag:
                break
        if flag:
            if num == 0:
                return [1, 0]
            else:
                return [0, 1]
        else:
            temp1 = check(x, y, length // 2)
            temp2 = check(x + length // 2, y, length // 2)
            temp3 = check(x, y + length // 2, length // 2)
            temp4 = check(x + length // 2, y + length // 2, length // 2)
            temp = [temp1[0] + temp2[0] + temp3[0] + temp4[0], temp1[1] + temp2[1] + temp3[1] + temp4[1]]
            return temp

    ans = check(0, 0, n)
    print(ans[0])
    print(ans[1])
    return

if __name__ == "__main__":
    main()