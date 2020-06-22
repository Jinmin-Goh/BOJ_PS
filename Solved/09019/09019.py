# Problem No.: 9019
# Solver:      Jinmin Goh
# Date:        20200619
# URL: https://www.acmicpc.net/problem/9019

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
import collections

def main():
    t = int(input())
    for _ in range(t):
        a, b = map(int, input().split())
        
        visited = [False] * 10000
        stack = collections.deque([(a, "")])
        ans = ""
        while stack:
            temp = stack.popleft()
            if temp[0] == b:
                ans = temp[1]
                break
            
            if visited[temp[0]]:
                continue
            visited[temp[0]] = True
            
            # D
            tempVal = (2 * temp[0]) % 10000
            if not visited[tempVal]:
                stack.append((tempVal, temp[1] + "D"))
            # S
            tempVal = (temp[0] - 1) % 10000
            if not visited[tempVal]:
                stack.append((tempVal, temp[1] + "S"))
            # L
            tempVal = (temp[0] % 1000) * 10 + temp[0] // 1000
            if not visited[tempVal]:
                stack.append((tempVal, temp[1] + "L"))
            # R
            tempVal = (temp[0] % 10) * 1000 + temp[0] // 10
            if not visited[tempVal]:
                stack.append((tempVal, temp[1] + "R"))
    
        
        print(ans)
        
    return

if __name__ == "__main__":
    main()