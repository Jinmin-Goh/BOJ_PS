# Problem No.: 1764
# Solver:      Jinmin Goh
# Date:        20200410
# URL: https://www.acmicpc.net/problem/1764

import sys

def main():
    n, m = map(int, input().split())
    nameSet = set()
    ans = []
    for _ in range(n):
        nameSet.add(str(sys.stdin.readline()))
    for _ in range(m):
        name = str(sys.stdin.readline())
        if name in nameSet:
            ans.append(name[:-1])
    ans.sort()
    #print(ans)
    print(len(ans))
    for i in ans:
        print(i)
    return

if __name__ == "__main__":
    main()