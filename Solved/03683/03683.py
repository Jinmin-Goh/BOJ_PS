# Problem No.: 3683
# Solver:      Jinmin Goh
# Date:        20220831
# URL: https://www.acmicpc.net/problem/3683

import sys

def solve(graph, check, arr, curr):
    for next in graph[curr]:
        if check[next]:
            continue
        check[next] = True
        if arr[next] == -1 or solve(graph, check, arr, arr[next]):
            arr[next] = curr
            return True
    return False

def main():
    t = int(sys.stdin.readline().rstrip())
    for _ in range(t):
        c, d, v = map(int, sys.stdin.readline().split())
        nums1 = []
        nums2 = []
        graph = [[] for _ in range(501)]
        arr = [-1 for _ in range(501)]
        for _ in range(v):
            a, b = map(str, sys.stdin.readline().split())
            nums1.append(a)
            nums2.append(b)
        for i in range(v - 1):
            for j in range(i + 1, v):
                if nums1[i] == nums2[j] or nums1[j] == nums2[i]:
                    if nums1[i][0] == 'C':
                        graph[i].append(j)
                    else:
                        graph[j].append(i)
        val = 0
        for i in range(v):
            check = [False for _ in range(501)]
            if solve(graph, check, arr, i):
                val += 1
        print(v - val)
    return

if __name__ == "__main__":
    main()