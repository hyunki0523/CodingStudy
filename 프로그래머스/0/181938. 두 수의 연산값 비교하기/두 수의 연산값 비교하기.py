def solution(a, b):
    sum = str(a)+str(b)
    if 2*a*b < int(sum):
        answer = int(sum)
        
    else:
        answer = 2*a*b
    return answer