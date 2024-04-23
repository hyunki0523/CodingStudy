def solution(n):
    answer = 0
    for j in range(4,n+1):
        cnt = 0
        for i in range(1,j+1):
            if j%i ==0:
                cnt += 1
                if cnt > 2:
                    answer += 1
                    break
        
    return answer