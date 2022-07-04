# Problem No.: 25315
# Solver:      Jinmin Goh
# Date:        20220704
# URL: https://www.acmicpc.net/problem/25315

import sys

def CCW(x1, y1, x2, y2, x3, y3):
    val = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)
    if val < 0:
        return -1
    elif val > 0:
        return 1
    else:
        return 0

def main():
    n = int(input())
    lines = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
    weight = []
    cnt = [0 for _ in range(n)]
    graph = [[] for _ in range(n)]
    for i in range(n):
        val = lines[i][4]
        for j in range(n):
            if i == j:
                continue
            x1, y1, x2, y2, w1 = lines[i]
            x3, y3, x4, y4, w2 = lines[j]
            if CCW(x1, y1, x2, y2, x3, y3) * CCW(x1, y1, x2, y2, x4, y4) < 0 and CCW(x3, y3, x4, y4, x1, y1) * CCW(x3, y3, x4, y4, x2, y2) < 0:
                cnt[i] += 1
                graph[i].append(j)
        weight.append((val, i))
    weight.sort()
    ans = 0
    p = 0
    for w, i in weight:
        ans += lines[i][4] * (cnt[i] + 1)
        for node in graph[i]:
            cnt[node] -= 1
    print(ans)
    return

if __name__ == "__main__":
    main()