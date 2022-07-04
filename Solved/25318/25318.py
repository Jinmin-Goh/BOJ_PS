# Problem No.: 25318
# Solver:      Jinmin Goh
# Date:        20220704
# URL: https://www.acmicpc.net/problem/25318

import sys
from datetime import datetime

def main():
    n = int(input())
    if n == 0:
        print(0)
        return
    times = []
    for _ in range(n):
        d, t, w = map(str, sys.stdin.readline().split())
        time = datetime.strptime(d + ' ' + t, "%Y/%m/%d %H:%M:%S")
        times.append((time, int(w)))
    t_N = times[-1][0]
    p_list = [max(0.9 ** (n - (i + 1)), 0.5 ** ((t_N - times[i][0]).seconds / (365 * 24 * 60 * 60) + (t_N - times[i][0]).days / 365)) for i in range(n)]
    p_sum = sum(p_list)
    ans = 0
    for i in range(n):
        ans += p_list[i] * times[i][1]
    ans /= p_sum
    ans = round(ans)
    print(ans)
    return

if __name__ == "__main__":
    main()