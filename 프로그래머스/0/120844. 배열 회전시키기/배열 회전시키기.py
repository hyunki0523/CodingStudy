def solution(numbers, direction):
    answer = []
    a = 0
    if direction =="right" :
        a = numbers.pop()
        answer.append(a)
        for i in numbers:
            answer.append(i)
    else :
        a = numbers.pop(0)
        for i in numbers:
            answer.append(i) 
        answer.append(a)
    return answer