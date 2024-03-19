def solution(my_string, is_suffix):
    if len(is_suffix) <= len(my_string) and is_suffix == my_string[-len(is_suffix):]:
        answer = 1
    else:
        answer = 0
    return answer
