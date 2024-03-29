def solution(numbers):
    answer = 0
    if len(numbers) == 2:
        answer = numbers[0] * numbers[1]
    else:
        for j in range(len(numbers)):
            for i in range(0, j):
                if answer < numbers[j] * numbers[i]:
                    answer = numbers[j] * numbers[i]
    return answer
