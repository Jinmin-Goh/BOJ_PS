# Problem No.: 14572
# Solver:      Jinmin Goh
# Date:        20220823
# URL: https://www.acmicpc.net/problem/14572

import sys

def main():
    n, k, d = map(int, sys.stdin.readline().split())
    student = []
    for _ in range(n):
        student.append(list(map(int, sys.stdin.readline().split())))
        student[-1].append(list(map(int, sys.stdin.readline().split())))
    student.sort(key=lambda x:x[1])
    p1 = 0
    p2 = 0
    algorithm = [0 for _ in range(31)]
    ans = 0
    for i in student[0][2]:
        algorithm[i] += 1
    while p1 < n:
        while p2 + 1 < n and student[p2 + 1][1] - student[p1][1] <= d:
            p2 += 1
            for i in student[p2][2]:
                algorithm[i] += 1
        val1 = 0
        val2 = 0
        for i in range(1, 31):
            if algorithm[i] != 0:
                if algorithm[i] == p2 - p1 + 1:
                    val2 += 1
                val1 += 1
        ans = max(ans, (val1 - val2) * (p2 - p1 + 1))
        for i in student[p1][2]:
            algorithm[i] -= 1
        p1 += 1
    print(ans)
        
        
    return

if __name__ == "__main__":
    main()