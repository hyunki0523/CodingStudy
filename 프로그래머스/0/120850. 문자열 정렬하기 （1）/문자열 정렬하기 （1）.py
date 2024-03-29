def solution(my_string):
    answer = []
    for i in my_string:
        if not i.isalpha():
            answer.append(int(i))
    answer.sort()
    return answer