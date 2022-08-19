# Problem No.: 10999
# Solver:      Jinmin Goh
# Date:        20220819
# URL: https://www.acmicpc.net/problem/10999

import sys
sys.setrecursionlimit(10 ** 5)

class SegTree():
    def __init__(self):
        self.nums = [0 for _ in range(4000010)]

    def update(self, val, idx, n, l, r):
        if idx <= l and r <= idx:
            self.nums[n] += val
            return
        elif idx < l or r < idx:
            return
        m = (l + r) // 2
        self.update(val, idx, 2 * n, l, m)
        self.update(val, idx, 2 * n + 1, m + 1, r)
        self.nums[n] = self.nums[2 * n] + self.nums[2 * n + 1]
        return
    
    def get_val(self, ql, qr, n, l, r):
        if ql <= l and r <= qr:
            return self.nums[n]
        elif qr < l or r < ql:
            return 0
        m = (l + r) // 2
        l_val = self.get_val(ql, qr, 2 * n, l, m)
        r_val = self.get_val(ql, qr, 2 * n + 1, m + 1, r)
        return l_val + r_val

def main():
    n, m, k = map(int, sys.stdin.readline().split())
    nums = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
    p_tree = SegTree()
    q_tree = SegTree()
    nums_sum = [nums[0]]
    for i in range(1, n):
        nums_sum.append(nums_sum[-1] + nums[i])
    for i in range(1, n):
        q_tree.update(nums_sum[i] - nums_sum[i - 1], i + 1, 1, 1, n)
    q_tree.update(nums_sum[0], 1, 1, 1, n)
    for _ in range(m + k):
        query = list(map(int, sys.stdin.readline().split()))
        if query[0] == 1:
            _, a, b, c = query
            p_tree.update(c, a, 1, 1, n)
            p_tree.update(-c, b + 1, 1, 1, n)
            q_tree.update((-a + 1) * c, a, 1, 1, n)
            q_tree.update(b * c, b + 1, 1, 1, n)
        else:
            _, a, b = query
            l_val = p_tree.get_val(1, a - 1, 1, 1, n) * (a - 1) + q_tree.get_val(1, a - 1, 1, 1, n)
            r_val = p_tree.get_val(1, b, 1, 1, n) * b + q_tree.get_val(1, b, 1, 1, n)
            print(r_val - l_val)
    return

if __name__ == "__main__":
    main()