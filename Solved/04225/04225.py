# Problem No.: 4225
# Solver:      Jinmin Goh
# Date:        20220805
# URL: https://www.acmicpc.net/problem/4225

import sys, functools, math

def comp(dot1, dot2):
    if dot1[3] * dot2[2] != dot1[2] * dot2[3]:
        if dot1[3] * dot2[2] < dot1[2] * dot2[3]:
            return 1
        else:
            return -1
    if dot1[2] ** 2 + dot1[3] ** 2 < dot2[2] ** 2 + dot2[3] ** 2:
        return 1
    else:
        return -1

def ccw(a, b, c):
    val1 = a[0] * b[1] + b[0] * c[1] + c[0] * a[1]
    val2 = b[0] * a[1] + c[0] * b[1] + a[0] * c[1]
    if (val1 - val2) > 0:
        return 1
    elif (val1 - val2) < 0:
        return -1
    else:
        return 0

def distance(dot, dot1, dot2):
    line_len = ((dot1[0] - dot2[0]) ** 2 + (dot1[1] - dot2[1]) ** 2) ** 0.5
    return abs((dot1[1] - dot[1]) * (dot2[0] - dot1[0]) - (dot1[0] - dot[0]) * (dot2[1] - dot1[1])) / line_len

def main():
    n = int(sys.stdin.readline().rstrip())
    cnt = 1
    while n != 0:
        dots = [[0, 0, 0, 0] for _ in range(n)]
        for i in range(n):
            dots[i][0], dots[i][1] = map(int, sys.stdin.readline().split())
        dots.sort(key=lambda x:(x[1], x[0]))
        dot = dots[0]
        for i in range(1, n):
            dots[i][2] = dots[i][0] - dot[0]
            dots[i][3] = dots[i][1] - dot[1]
        dots.sort(key=functools.cmp_to_key(comp))
        dots = list(reversed(dots))
        stack = [0, 1]
        t = 1
        idx = 2
        while idx < n:
            val = ccw(dots[stack[t - 1]], dots[stack[t]], dots[idx])
            if val > 0:
                stack.append(idx)
                idx += 1
                t += 1
            elif val == 0:
                stack.pop()
                stack.append(idx)
                idx += 1
            else:
                stack.pop()
                t -= 1
        convex_hull = [(dots[stack[i]][0], dots[stack[i]][1]) for i in range(len(stack))]
        ans = 100000000
        m = len(convex_hull)
        for i in range(m):
            temp = 0
            for j in range(m):
                temp = max(temp, distance(convex_hull[j], convex_hull[i % m], convex_hull[(i + 1) % m]))
            ans = min(ans, temp)
        ans_int = int(ans * 100)
        if ans * 100 - ans_int > 0:
            ans_int += 1
        print(f"Case {cnt}: {ans_int / 100:.2f}")
        cnt += 1
        n = int(sys.stdin.readline().rstrip())
    return

if __name__ == "__main__":
    main()