# Problem No.: 1919
# Solver:      Jinmin Goh
# Date:        20220703
# URL: https://www.acmicpc.net/problem/1919

import sys

def main():
    s1 = input()
    s2 = input()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    s1_dict = {i:0 for i in alphabet}
    s2_dict = {i:0 for i in alphabet}
    for i in s1:
        s1_dict[i] += 1
    for i in s2:
        s2_dict[i] += 1
    ans = 0
    for i in alphabet:
        ans += abs(s1_dict[i] - s2_dict[i])
    print(ans)
    return

if __name__ == "__main__":
    main()