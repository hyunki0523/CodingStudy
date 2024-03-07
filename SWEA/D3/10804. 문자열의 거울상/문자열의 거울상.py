N = int(input())
for j in range(N):
    text =input()
    result = ''
    reversed_text = text[::-1]
    for i in reversed_text:
        if i =='q':
            result += 'p'
        elif i == 'p':
            result += 'q'
        elif i == 'b':
            result += 'd'
        else: #i == 'd':
            result += 'b'
    print(f'#{j+1} {result}')