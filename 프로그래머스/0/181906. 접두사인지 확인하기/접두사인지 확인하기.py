def solution(my_string, is_prefix):
    answer = 0
    if len(is_prefix) <= len(my_string) and my_string.startswith(is_prefix):
        answer = 1
    return answer
