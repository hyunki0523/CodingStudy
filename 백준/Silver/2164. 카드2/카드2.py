from collections import deque
N = int(input())
arr = deque()
val = 0

for i in range(N):
    arr.append(i+1)
for j in range(N-1):
    arr.popleft()
    val = arr.popleft()
    arr.append(val)
print(arr[0])