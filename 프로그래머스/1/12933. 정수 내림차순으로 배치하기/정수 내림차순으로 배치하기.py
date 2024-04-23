def solution(n):
    answer = []
    for i in str(n):
        answer.append(int(i))
    answer.sort(reverse=True)
    return int(''.join(map(str, answer)))