def solution(myString, pat):
    convertPat = ''
    answer = 0
    for i in pat:
        if i == "A":
            convertPat += "B"
        else :
            convertPat += "A"
    print(convertPat)
    if convertPat in myString:
        answer = 1
    elif len(convertPat) == len(myString):
        answer = 0    
    return answer