# Problem No.: 14725
# Solver:      Jinmin Goh
# Date:        20220707
# URL: https://www.acmicpc.net/problem/14725

import sys

class Node:
    def __init__(self, key):
        self.key = key
        self.data = False
        self.children = {}

    def print_func(self, node, depth):
        key_list = list(node.children.keys())
        key_list.sort()
        for key in key_list:
            print('--' * depth + key)
            node.print_func(node.children[key], depth + 1)

class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, s_list):
        curr_node = self.head
        for s in s_list:
            if s not in curr_node.children:
                curr_node.children[s] = Node(s)
            curr_node = curr_node.children[s]
        curr_node.data = True
    
    

def main():
    n = int(input())
    s_list = [list(map(str, sys.stdin.readline().split())) for _ in range(n)]
    t = Trie()
    for i in range(n):
        t.insert(s_list[i][1:])
    t.head.print_func(t.head, 0)
    return

if __name__ == "__main__":
    main()