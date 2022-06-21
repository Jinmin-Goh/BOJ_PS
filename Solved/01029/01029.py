# Problem No.: 1029
# Solver:      Jinmin Goh
# Date:        20220621
# URL: https://www.acmicpc.net/problem/1029

import sys

def main():
    n = int(input())
    cost = [[int(i) for i in list(input())] for _ in range(n)]
    dp_table = [[1000000 for _ in range (1 << n)] for __ in range(n)]
    queue = [(0, 0, 1, 1)]
    ans = 1
    while queue:
        temp = []
        for buyer, price, sellers, num in queue:
            for j in range(n):
                # if j didn't selled before
                if (not sellers & (1 << j)) and price <= cost[buyer][j]:
                    if dp_table[j][sellers | (1 << j)] > cost[buyer][j]:
                        dp_table[j][sellers | (1 << j)] = cost[buyer][j]
                        ans = max(ans, num + 1)
                        temp.append((j, cost[buyer][j], sellers | (1 << j), num + 1))
        queue = temp
    print(ans)
    return

if __name__ == "__main__":
    main()