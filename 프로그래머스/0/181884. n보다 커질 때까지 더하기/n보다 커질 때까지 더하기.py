def solution(numbers, n):
    answer = 0
    for i in numbers:
        if answer > n:
            break
        else :
            answer += i
    return answer