def solution(arr):
    answer = 0
    cnt = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] == arr[j][i]:
                cnt += 1
    if cnt == len(arr) **2 :
        answer = 1
    return answer