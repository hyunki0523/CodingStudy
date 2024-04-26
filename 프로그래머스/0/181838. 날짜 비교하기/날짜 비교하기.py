def solution(date1, date2):
    datesum1=0
    datesum2=0
    datesum1=date1[0]*365 + date1[1]*30.5 + date1[2]
    datesum2=date2[0]*365 + date2[1]*30.5 + date2[2]
    if datesum1 < datesum2:
        answer = 1
    else :
        answer = 0
    return answer