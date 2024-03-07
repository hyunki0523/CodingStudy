def solution(my_string):
    answer = ''
    moum = {'a','e','i','o','u'}
    for i in my_string:
        if i not in moum:
            answer += i
    return answer