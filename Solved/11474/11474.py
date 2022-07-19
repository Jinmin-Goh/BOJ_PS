# Problem No.: 11474
# Solver:      Jinmin Goh
# Date:        20220719
# URL: https://www.acmicpc.net/problem/11474

import sys, random, math

def main():
    random.seed(3215463215)
    n, m = map(int, sys.stdin.readline().split())
    triple = [tuple(map(int, sys.stdin.readline().split())) for _ in range(m)]
    rand = list(range(1, n+1))
    random.shuffle(rand)
    idx = [-1 for _ in range(n + 1)]
    for i in range(n):
        idx[rand[i]] = i
    t = 1
    val = math.isqrt(10 ** 7 * 3 // n)
    while True:
        if t % val == 0:
            rand = []
            rand = list(range(1, n+1))
            random.shuffle(rand)
            idx = [-1 for _ in range(n + 1)]
            for i in range(n):
                idx[rand[i]] = i
        cnt = 0
        unsatisfy = []
        for a, b, c in triple:
            if min(idx[a], idx[c]) < idx[b] < max(idx[a], idx[c]):
                cnt += 1
            else:
                unsatisfy.append((a, b, c))
        if cnt >= (m + 1) // 2:
            for i in rand:
                print(i, end=' ')
            break
        else:
            for a, b, c in unsatisfy:
                if min(idx[a], idx[c]) < idx[b] < max(idx[a], idx[c]):
                    continue
                if idx[a] > idx[c]:
                    if idx[a] < idx[b]:
                        rand[idx[b]], rand[idx[a]] = rand[idx[a]], rand[idx[b]]
                        idx[b], idx[a] = idx[a], idx[b]
                    else:
                        rand[idx[b]], rand[idx[c]] = rand[idx[c]], rand[idx[b]]
                        idx[b], idx[c] = idx[c], idx[b]
                else:
                    if idx[c] < idx[b]:
                        rand[idx[b]], rand[idx[c]] = rand[idx[c]], rand[idx[b]]
                        idx[b], idx[c] = idx[c], idx[b]
                    else:
                        rand[idx[b]], rand[idx[a]] = rand[idx[a]], rand[idx[b]]
                        idx[b], idx[a] = idx[a], idx[b]
        t += 1
    return

if __name__ == "__main__":
    main()