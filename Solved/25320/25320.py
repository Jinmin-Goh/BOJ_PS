# Problem No.: 25320
# Solver:      Jinmin Goh
# Date:        20220705
# URL: https://www.acmicpc.net/problem/25320

import sys
sys.setrecursionlimit(200010)

def union(parent, x, y):
    x = find(parent, x)
    y = find(parent, y)
    if x == y:
        return
    elif x < y:
        parent[x] = y
    else:
        parent[y] = x

def find(parent, x):
    if parent[x] == -1:
        return -1
    if x == parent[x]:
        return x
    parent[x] = find(parent, parent[x])
    return parent[x]

def main():
    n, m = map(int, input().split())
    block = []
    for _ in range(m):
        a, b, i = map(str, sys.stdin.readline().split())
        block.append((a, b, int(i) - 1))
    valid = [-1 for _ in range(2 * n)]
    temp = []
    if block[0][0] == 'B':
        print("NO")
        return
    # check used numbers
    for a, _, i in block:
        valid[i] = i
        if i > 0 and find(valid, i - 1) != -1:
            union(valid, i, i - 1)
        if i < 2 * n - 1 and find(valid, i + 1) != -1:
            union(valid, i, i + 1)
    
    for i in range(m):
        temp.append(block[i])
        if (i < m - 1 and block[i][0] == block[i + 1][0]) or (i == m - 1 and block[i][0] == 'A'):
            p = block[i][2] + 1
            if p >= 2 * n:
                print("NO")
                return
            if find(valid, p) == -1:
                valid[p] = p
                union(valid, p, p - 1)
                if p < 2 * n - 1 and find(valid, p + 1) != -1:
                    union(valid, p, p + 1)
                temp.append(('A' if block[i][0] == 'B' else 'B', 'CHAIN', p))
            else:
                p = find(valid, p) + 1
                if p >= 2 * n:
                    print("NO")
                    return
                else:
                    valid[p] = p
                    union(valid, p, p - 1)
                    if p < 2 * n - 1 and find(valid, p + 1) != -1:
                        union(valid, p, p + 1)
                    temp.append(('A' if block[i][0] == 'B' else 'B', 'CHAIN', p))
    i = 0
    cnt = 0
    temp_valid = valid[:]
    while i < len(temp):
        cnt += 1
        if temp[i][2] == 0:
            if i < len(temp) - 1 and temp[i + 1][1] == 'CHAIN':
                i += 1
                cnt += 1
            p = find(temp_valid, temp[i][2]) + 1
            while p < 2 * n:
                cnt += 1
                temp_valid[p] = p
                union(temp_valid, p, p - 1)
                if p < 2 * n - 1 and find(temp_valid, p + 1) != -1:
                    union(temp_valid, p, p + 1)
                p = find(temp_valid, p) + 1
        i += 1
    if cnt == 2 * n:
        i = 0
        print("YES")
        while i < len(temp):
            a, c, num = temp[i]
            print(f"{a} {c} {num + 1}")
            if temp[i][2] == 0:
                if i < len(temp) - 1 and temp[i + 1][1] == 'CHAIN':
                    i += 1
                    a, c, num = temp[i]
                    print(f"{a} {c} {num + 1}")
                p = find(valid, temp[i][2]) + 1
                while p < 2 * n:
                    a, c, num = 'A' if a == 'B' else 'B', 'CHAIN', p
                    print(f"{a} {c} {num + 1}")
                    valid[p] = p
                    union(valid, p, p - 1)
                    if p < 2 * n - 1 and find(valid, p + 1) != -1:
                        union(valid, p, p + 1)
                    p = find(valid, p) + 1
            i += 1
    else:
        print("NO")
    return

if __name__ == "__main__":
    main()