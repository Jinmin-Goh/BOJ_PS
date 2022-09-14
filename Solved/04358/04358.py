# Problem No.: 4358
# Solver:      Jinmin Goh
# Date:        20220914
# URL: https://www.acmicpc.net/problem/4358

import sys

def main():
    tree_dict = {}
    total = 0
    temp = sys.stdin.readline().rstrip()
    while temp:
        if temp not in tree_dict:
            tree_dict[temp] = 0
        tree_dict[temp] += 1
        total += 1
        temp = sys.stdin.readline().rstrip()
    tree_list = list(tree_dict.keys())
    tree_list.sort()
    for tree in tree_list:
        print(f"{tree} {tree_dict[tree] / total * 100:.4f}")
    return

if __name__ == "__main__":
    main()