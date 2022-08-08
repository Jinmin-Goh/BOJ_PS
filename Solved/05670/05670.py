# Problem No.: 5670
# Solver:      Jinmin Goh
# Date:        20220808
# URL: https://www.acmicpc.net/problem/5670

import sys

class Node():
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}

    def search(self, node, cnt):
        val = 0
        key_list = list(node.children.keys())
        if node.data != None:
            val += cnt
        if len(key_list) > 1 or node.data != None:
            cnt += 1
        for key in key_list:
            val += node.search(node.children[key], cnt)
        return val
    
class Trie():
    def __init__(self):
        self.head = Node(None)
    
    def insert(self, s):
        curr = self.head
        for char in s:
            if char not in curr.children:
                curr.children[char] = Node(char)
            curr = curr.children[char]
        curr.data = s

def main():
    n = sys.stdin.readline().rstrip()
    while n:
        n = int(n)
        words = [sys.stdin.readline().rstrip() for _ in range(n)]
        trie = Trie()
        for word in words:
            trie.insert(word)
        cnt = 0
        if len(trie.head.children) == 1:
            cnt += 1
        ans = trie.head.search(trie.head, cnt) / n
        print(f"{round(ans, 2):.2f}")
        n = sys.stdin.readline().rstrip()
    return

if __name__ == "__main__":
    main()