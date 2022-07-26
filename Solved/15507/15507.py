# Problem No.: 15507
# Solver:      Jinmin Goh
# Date:        20220725
# URL: https://www.acmicpc.net/problem/15507

import sys

def main():
    n = int(sys.stdin.readline().rstrip())
    s = sys.stdin.readline().rstrip()
    candidate = []
    for i in range(20):
        if n % (2 ** i + 1) == 0:
            candidate.append((i, n // (2 ** i + 1)))
    if not candidate:
        print(-1)
        return
    ans = 10 ** 9
    hash_list = [0]
    pow_list = [1]
    for i in range(n):
        hash_list.append((hash_list[-1] * 11 + int(s[i]) + 7) % 1000000007)
        pow_list.append((pow_list[-1] * 11) % 1000000007)
    for a, b in candidate:
        cnt = 0
        stack = [(0, 0)]
        flag = False
        visited = [[False for _ in range(20)] for _ in range(n + 1)]
        while stack:
            temp = []
            for x, i in stack:
                if visited[x][i]:
                    continue
                visited[x][i] = True
                y = (2 ** i) * b + x
                if x == b and y == n and i == a:
                    flag = True
                    break
                if x < b and y < n and s[x] == s[y]:
                    temp.append((x + 1, i))
                if i < a and 2 * x <= b and 2 * y <= n and hash_list[x] == (hash_list[2 * x] - hash_list[x] * pow_list[x]) % 1000000007 and hash_list[y] == (hash_list[2 * y] - hash_list[y] * pow_list[y]) % 1000000007:
                    temp.append((2 * x, i + 1))
            if flag:
                break
            cnt += 1
            stack = temp
        del visited
        if flag:
            ans = min(ans, cnt)
    if ans == 10 ** 9:
        print(-1)
    else:
        print(ans)
    return

if __name__ == "__main__":
    main()