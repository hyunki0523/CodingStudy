def solution(binomial):
    
    binomial = binomial.split()
    num1 = int(binomial[0])
    operator = binomial[1]
    num2 = int(binomial[2])

    if operator == "+":
        answer = num1 + num2
    elif operator == "-":
        answer = num1 - num2
    else:
        answer = num1 * num2

    return answer
