from collections import deque
import sys
n = int(sys.stdin.readline())
queue = deque()
a = 0


for i in range(1, n+1):
    queue.append(i)



while len(queue) != 1:
    a += 1
    b = a**3
    for i in range(b % len(queue)):
        queue.append(queue.popleft())
    queue.pop()

print(queue.pop())
