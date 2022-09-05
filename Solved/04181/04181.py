# Problem No.: 4181
# Solver:      Jinmin Goh
# Date:        20220905
# URL: https://www.acmicpc.net/problem/4181

import sys, functools

def comp(dot1, dot2):
    if dot1[3] * dot2[2] != dot1[2] * dot2[3]:
        if dot1[3] * dot2[2] > dot1[2] * dot2[3]:
            return 1
        else:
            return -1
    if dot1[2] ** 2 + dot1[3] ** 2 > dot2[2] ** 2 + dot2[3] ** 2:
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
    n = int(sys.stdin.readline().rstrip())
    dots = []
    for _ in range(n):
        x, y, c = map(str, sys.stdin.readline().split())
        if c == 'Y':
            dots.append((int(x), int(y)))
    dots.sort(key=lambda x:(x[0], x[1]))
    dot = (dots[0][0], dots[0][1], 0, 0)
    for i in range(len(dots)):
        dots[i] = (dots[i][0], dots[i][1], dots[i][0] - dot[0], dots[i][1] - dot[1])
    dots.sort(key=functools.cmp_to_key(comp))
    cnt = len(dots) - 1
    while ccw(dot, dots[cnt], dots[cnt - 1]) == 0:
        cnt -= 1
    dots = dots[:cnt] + list(reversed(dots[cnt:]))
    print(len(dots))
    for x, y, _, _ in dots:
        print(x, y)
    return

if __name__ == "__main__":
    main()