def solution(x):
    answer = True
    digit = 0
    for i in str(x):
        digit += int(i)
    if x % digit !=0:
        answer = False   
    return answer