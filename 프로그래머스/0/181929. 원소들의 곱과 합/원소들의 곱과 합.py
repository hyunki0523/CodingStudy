def solution(num_list):
    answer = 0
    A =1
    B = sum(num_list)
    for i in num_list:
        A *= i
    if B**2 > A:
        answer = 1
    return answer