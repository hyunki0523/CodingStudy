def solution(arr, queries):
    answer = []
    for a in queries:
        s, e = a
        for i in range(s, e+1):
            arr[i] = arr[i]+1
    return arr