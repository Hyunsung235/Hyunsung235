import sys
memory = [1, 1, 1, 2, 2]
for i in range(int(sys.stdin.readline())):
    a = int(sys.stdin.readline())
    if a > len(memory) - 1:
        for j in range(a - (len(memory) - 1)):
            memory.append(memory[-1] + memory[len(memory) - 5])
    print(memory[a - 1])