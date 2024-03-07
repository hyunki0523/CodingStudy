def rep(x,y):
    if y == 0 :
        return 1
    else:
        result = x * rep(x,y - 1)
        return result
for i in range(1,11):
    N=0
    N = int(input())
    a, b = map(int,input().split())

    print(f'#{N}', rep(a,b))