# Problem No.: 18498
# Solver:      Jinmin Goh
# Date:        20220720
# URL: https://www.acmicpc.net/problem/18498

import sys, random

def main():
    n = int(sys.stdin.readline().rstrip())
    perm = list(range(1, n+1))
    batch = set()
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            batch.add((i, j))
    while True:
        print('?', end=' ')
        for i in perm:
            print(i, end=' ')
        print('')
        sys.stdout.flush()
        cnt = int(sys.stdin.readline().rstrip())
        if cnt == n - 1:
            print('!', end=' ')
            for i in perm:
                print(i, end=' ')
            print('')
            return
        if cnt == 0:
            for i in range(n - 1):
                if (perm[i], perm[i + 1]) in batch:
                    batch.remove((perm[i], perm[i + 1]))
                if (perm[i + 1], perm[i]) in batch:
                    batch.remove((perm[i + 1], perm[i]))
        if len(batch) == n - 1:
            break
        random.shuffle(perm)
    path = [[] for _ in range(n + 1)]
    batch = list(batch)
    for a, b in batch:
        path[a].append(b)
        path[b].append(a)
    pos = -1
    for i in range(n):
        if len(path[i]) == 1:
            pos = i
            break
    print('!', end=' ')
    print(pos, end=' ')
    visited = [False for _ in range(n + 1)]
    visited[pos] = True
    pos = path[pos][0]
    while True:
        print(pos, end=' ')
        visited[pos] = True
        if len(path[pos]) == 1:
            pos = path[pos][0]
            break
        else:
            pos = path[pos][0] if visited[path[pos][1]] else path[pos][1]
    return

if __name__ == "__main__":
    main()