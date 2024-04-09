def solution(myString):
    answer = []
    div = []
    for i in myString:
        if i == "x":
            answer.append("".join(div))
            div = []
        else:
            div.append(i)
    answer.append("".join(div))
    answer = sorted(answer)
    answer = [item for item in answer if item != ""]
    return answer
