def solution(num_list, n):
    answer = []
    for i in range(n):
        A = num_list.pop(0)
        num_list.append(A)
    answer = num_list
    return answer