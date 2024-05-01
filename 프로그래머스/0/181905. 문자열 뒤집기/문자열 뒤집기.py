def solution(my_string, s, e):
    answer = ''
    for i in range(0,s):
        answer += my_string[i]
    for j in range(e,s-1,-1):
        answer += my_string[j]
    for k in range(e+1,len(my_string)):
        answer += my_string[k]
    return answer