def solution(myString):
    answer = ''
    myString = myString.lower()
    for i in myString:
        if i == 'a':
            answer += 'A'
        else:
            answer += i
    return answer