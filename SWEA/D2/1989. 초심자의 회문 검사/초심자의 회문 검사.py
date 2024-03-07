T = int(input())
for case in range(1,T+1,+1):
    text =input()
    reversed_text = text[::-1]
    if text== reversed_text:
        result = 1
        print(f'#{case} {result}')
    else:
        result = 0
        print(f'#{case} {result}')