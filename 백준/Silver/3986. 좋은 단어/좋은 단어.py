
N = int(input())

cnt = 0
for i in range(N):
    Text = input()
    stack = []
    for j in Text:
        if len(stack) == 0 :
            stack.append(j)
        else:
            if j == "A":
                if stack[-1] == "B":
                    stack.append(j)
                    
                elif stack[-1] == "A":
                    stack.pop()
            elif j =="B": #B 인경우
                if stack[-1] == "A":
                    stack.append(j)
                elif stack[-1] == "B":
                    stack.pop()
    if len(stack) == 0:
        cnt += 1
print(cnt)
