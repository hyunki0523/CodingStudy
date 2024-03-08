N = int(input())

for i in range(N):
    Text = []
    a = input()
    for j in a:
        if j == '(':
            Text.append(j)
        elif j == ')':
            if Text:
                Text.pop()
            else:
                print("NO")
                break
    else:
        if not Text:
            print("YES")
        else:
            print("NO")