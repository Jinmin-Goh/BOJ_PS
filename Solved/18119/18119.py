# Problem No.: 18119
# Solver:      Jinmin Goh
# Date:        20200506
# URL: https://www.acmicpc.net/problem/18119

##### FAST INPUT #####
import os
import sys
from io import BytesIO, IOBase

BUFSIZE = 8192


class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")


sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")
##### END OF FAST INPUT #####

#import sys

def main():
    n, m = map(int, input().split())
    alphabetDict = [[] for _ in range(26)]
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    mask = 2 ** 26 - 1
    wordList = [mask] * n
    for _ in range(n):
        word = input()
        word = list(set(word))
        for i in word:
            alphabetDict[alphabet.index(i)].append(_)
    ans = n
    for _ in range(m):
        a, b = input().split()
        pos = alphabet.index(b)
        for i in alphabetDict[alphabet.index(b)]:
            if a == "1":
                if wordList[i] & mask == mask:
                    ans -= 1
                wordList[i] &= ~(1 << pos)
            if a == "2":
                temp = wordList[i]
                wordList[i] |= (1 << pos)
                if temp != mask and wordList[i] & mask == mask:
                    ans += 1
        print(ans)
    return

if __name__ == "__main__":
    main()