def solution(sides):
    side = list(sides)
    side.sort()  
    if side[2] < side[1] + side[0]:  # 수정된 비교
        answer = 1
    else:
        answer = 2
    return answer
