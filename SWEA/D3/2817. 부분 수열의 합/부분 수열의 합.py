
T = int(input())
for i in range(T):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))

    def soo(N, K, arr, n, Sum):
        if n == N:
            return 0
        cnt = 0
        for i in range(n, N):
            Sum += arr[i]
            if Sum < K:
                cnt += soo(N, K, arr, i + 1, Sum)
            elif Sum == K:
                cnt += 1
            Sum -= arr[i]
        return cnt
    print(f'#{i+1} {soo(N, K, arr, 0, 0)}')
