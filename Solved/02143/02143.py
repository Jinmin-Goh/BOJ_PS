# Problem No.: 2143
# Solver:      Jinmin Goh
# Date:        20220630
# URL: https://www.acmicpc.net/problem/2143

import sys

def main():
    t = int(input())
    n = int(input())
    n_nums = list(map(int, sys.stdin.readline().split()))
    m = int(input())
    m_nums = list(map(int, sys.stdin.readline().split()))
    # prefix sum
    n_sums_front = [0 for _ in range(n)]
    n_sums_front[0] = n_nums[0]
    n_sums_back = [0 for _ in range(n)]
    n_sums_back[-1] = n_nums[-1]
    m_sums_front = [0 for _ in range(m)]
    m_sums_front[0] = m_nums[0]
    m_sums_back = [0 for _ in range(m)]
    m_sums_back[-1] = m_nums[-1]
    for i in range(1, n):
        n_sums_front[i] = n_sums_front[i - 1] + n_nums[i]
        n_sums_back[-i - 1] = n_sums_back[-i] + n_nums[-i - 1]
    for i in range(1, m):
        m_sums_front[i] = m_sums_front[i - 1] + m_nums[i]
        m_sums_back[-i - 1] = m_sums_back[-i] + m_nums[-i - 1]
    # all subarray sum
    n_sum = n_sums_back[0]
    m_sum = m_sums_back[0]
    n_sums = {}
    m_sums = {}
    for i in range(n):
        for j in range(i, n):
            val = n_sum
            if i != 0:
                val -= n_sums_front[i - 1]
            if j != n - 1:
                val -= n_sums_back[j + 1]
            if val not in n_sums:
                n_sums[val] = 0
            n_sums[val] += 1
    for i in range(m):
        for j in range(i, m):
            val = m_sum
            if i != 0:
                val -= m_sums_front[i - 1]
            if j != m - 1:
                val -= m_sums_back[j + 1]
            if val not in m_sums:
                m_sums[val] = 0
            m_sums[val] += 1
    ans = 0
    for i in n_sums:
        if t - i in m_sums:
            ans += n_sums[i] * m_sums[t - i]
    print(ans)
    return

if __name__ == "__main__":
    main()