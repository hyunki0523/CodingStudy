def solution(number):
    answer = 0
    sum = 0 
    for i in str(number):
        sum += int(i)
        answer = sum % 9
    return answer