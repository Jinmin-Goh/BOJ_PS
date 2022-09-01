# Problem No.: 10254
# Solver:      Jinmin Goh
# Date:        20220901
# URL: https://www.acmicpc.net/problem/10254

import sys, functools

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

def dist(dot1, dot2):
    return (dot1[0] - dot2[0]) ** 2 + (dot1[1] - dot2[1]) ** 2

def check(a, b, c, d):
    p1 = [a[0] - b[0], a[1] - b[1]]
    p2 = [c[0] - d[0], c[1] - d[1]]
    return ccw([0, 0], p1, p2)

def main():
    t = int(sys.stdin.readline().rstrip())
    for _ in range(t):
        n = int(sys.stdin.readline().rstrip())
        dots = []
        for _ in range(n):
            a, b = map(int, sys.stdin.readline().split())
            dots.append([a, b])
        dots.sort(key=lambda x:(x[1], x[0]))
        lower = []
        for d in dots:
            while len(lower) >= 2 and ccw(lower[-2], lower[-1], d) <= 0:
                lower.pop()
            lower.append(d)
        upper = []
        for d in reversed(dots):
            while len(upper) >= 2 and ccw(upper[-2], upper[-1], d) <= 0:
                upper.pop()
            upper.append(d)
        convex_hull = lower[:-1] + upper[:-1]
        N = len(convex_hull)
        val = 0
        j = 1
        ans1 = convex_hull[0]
        ans2 = convex_hull[1]
        for i in range(N):
            while j + 1 != i and check(convex_hull[i], convex_hull[(i + 1) % N], convex_hull[j % N], convex_hull[(j + 1) % N]) > 0:
                if dist(convex_hull[i], convex_hull[j % N]) > val:
                    ans1 = convex_hull[i]
                    ans2 = convex_hull[j % N]
                    val = dist(convex_hull[i], convex_hull[j % N])
                j += 1
            if dist(convex_hull[i], convex_hull[j % N]) > val:
                ans1 = convex_hull[i]
                ans2 = convex_hull[j % N]
                val = dist(convex_hull[i], convex_hull[j % N])
        print(ans1[0], ans1[1], ans2[0], ans2[1])
    return

if __name__ == "__main__":
    main()