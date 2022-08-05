# Problem No.: 3679
# Solver:      Jinmin Goh
# Date:        20220804
# URL: https://www.acmicpc.net/problem/3679

import sys, functools

def comp(dot1, dot2):
    if dot1[3] * dot2[2] != dot1[2] * dot2[3]:
        if dot1[3] * dot2[2] < dot1[2] * dot2[3]:
            return 1
        else:
            return -1
    if dot1[1] < dot2[1]:
        return 1
    else:
        return -1

def ccw(a, b, c):
    val1 = a[2] * b[3] + b[2] * c[3] + c[2] * a[3]
    val2 = b[2] * a[3] + c[2] * b[3] + a[2] * c[3]
    if ((val1 - val2) > 0):
        return 1
    elif ((val1 - val2) < 0):
        return -1
    else:
        return 0

def main():
    t = int(sys.stdin.readline().rstrip())
    for _ in range(t):
        nums = list(map(int, sys.stdin.readline().split()))
        n = nums[0]
        dots = [[nums[2 * i + 1], nums[2 * i + 2], 0, 0, i] for i in range(n)]
        dots.sort(key=lambda x:(x[1], x[0]))
        dot = dots[0]
        for i in range(1, n):
            dots[i][2] = dots[i][0] - dot[0]
            dots[i][3] = dots[i][1] - dot[1]
        dots.sort(key=functools.cmp_to_key(comp))
        cnt = 0
        dots = list(reversed(dots[:-1]))
        flag = False
        print(dot[4], end=' ')
        while ccw(dot, dots[cnt], dots[cnt + 1]) == 0:
            flag = True
            print(dots[cnt][4], end=' ')
            cnt += 1
        if flag:
            print(dots[cnt][4], end=' ')
            cnt += 1
        temp = list(reversed(dots[cnt:]))
        for _, _, _, _, i in temp:
            print(i, end=' ')
        print()
    return

if __name__ == "__main__":
    main()