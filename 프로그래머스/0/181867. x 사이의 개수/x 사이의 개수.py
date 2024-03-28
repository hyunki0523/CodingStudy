def solution(myString):
    answer = []
    Cnt = 0
    for i in myString:
        if i =='x':
            answer.append(Cnt)
            Cnt = 0
        else :
            Cnt += 1
    answer.append(Cnt)
    return answer