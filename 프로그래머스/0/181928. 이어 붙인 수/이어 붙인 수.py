def solution(num_list):
    answer = ''
    sum = ''
    for i in num_list:
        if i % 2 != 0:
            answer += str(i)
        else :
            sum += str(i)
    answer = int(answer) + int(sum)
    return answer