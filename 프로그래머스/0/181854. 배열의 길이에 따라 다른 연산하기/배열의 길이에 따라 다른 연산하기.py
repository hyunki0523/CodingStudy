def solution(arr, n):
    answer = []
    M = len(arr)
    if M % 2 ==0 :
        for i in range(1,M,+2):
            arr[i] = arr[i]+n
    else:
        for j in range(0,M,+2):
            arr[j] = arr[j]+n        
    answer = arr               
    return answer