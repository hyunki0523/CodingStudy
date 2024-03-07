def solution(n):
    answer = 2
    for i in range(n+1):
        if i*i == n:
            answer = 1
        else:
            pass
    return answer