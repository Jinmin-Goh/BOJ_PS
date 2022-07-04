# Problem No.: 25319
# Solver:      Jinmin Goh
# Date:        20220704
# URL: https://www.acmicpc.net/problem/25319

import sys

def main():
    n, m, s = map(int, input().split())
    table = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
    s = sys.stdin.readline().rstrip()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    coordinates = {i:[] for i in alphabet}
    table_cnt = {i:0 for i in alphabet}
    s_cnt = {i:0 for i in alphabet}
    for i in range(n):
        for j in range(m):
            coordinates[table[i][j]].append((i, j))
            table_cnt[table[i][j]] += 1
    for i in s:
        s_cnt[i] += 1
    c = 1000000
    for i in s_cnt:
        if s_cnt[i]:
            c = min(c, table_cnt[i] // s_cnt[i])
    ans = []
    x, y = 0, 0
    for _ in range(c):
        for i in s:
            new_x, new_y = coordinates[i].pop()
            if x > new_x:
                ans.append('U' * abs(new_x - x))
            else:
                ans.append('D' * abs(new_x - x))
            if y > new_y:
                ans.append('L' * abs(new_y - y))
            else:
                ans.append('R' * abs(new_y - y))
            ans.append('P')
            x = new_x
            y = new_y
    new_x, new_y = n - 1, m - 1
    if x > new_x:
        ans.append('U' * abs(new_x - x))
    else:
        ans.append('D' * abs(new_x - x))
    if y > new_y:
        ans.append('L' * abs(new_y - y))
    else:
        ans.append('R' * abs(new_y - y))
    ans = ''.join(ans)
    print(c, len(ans))
    print(ans)
    return

if __name__ == "__main__":
    main()