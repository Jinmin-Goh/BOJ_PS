# Problem No.: 10266
# Solver:      Jinmin Goh
# Date:        20220822
# URL: https://www.acmicpc.net/problem/10266

import sys

def main():
    n = int(sys.stdin.readline().rstrip())
    nums1 = list(map(int, sys.stdin.readline().split()))
    nums2 = list(map(int, sys.stdin.readline().split()))
    nums1.sort()
    nums2.sort()
    nums1 = [(nums1[(i + 1) % n] - nums1[i]) % 360000 for i in range(n)]
    nums2 = [(nums2[(i + 1) % n] - nums2[i]) % 360000 for i in range(n)]
    # KMP
    j = 0
    pi = [0 for _ in range(n)]
    for i in range(1, n):
        while j > 0 and nums2[i] != nums2[j]:
            j = pi[j - 1]
        if nums2[i] == nums2[j]:
            j += 1
            pi[i] = j
    for i in range(2 * n):
        while j > 0 and nums1[i % n] != nums2[j]:
            j = pi[j - 1]
        if nums1[i % n] == nums2[j]:
            j += 1
            if j == n:
                print("possible")
                return
    print("impossible")
    
    # or, use python 'in'
    # nums1 = [str(i) for i in nums1]
    # nums2 = [str(i) for i in nums2]
    # nums1 = ' '.join(nums1 + nums1)
    # nums2 = ' '.join(nums2)
    # if nums2 in nums1:
    #     print("possible")
    # else:
    #     print("impossible")
    # return

if __name__ == "__main__":
    main()