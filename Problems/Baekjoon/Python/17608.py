import sys

count = 1
l = int(sys.stdin.readline())
stack = [int(sys.stdin.readline()) for _ in range(l)]


a = stack.pop()
for i in range(l - 1):
    b = stack.pop()
    if a < b:
        count += 1
        a = b



print(count)