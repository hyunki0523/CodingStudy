def solution(s):
    answer = True
    cnt = 50
    for i in s:
        if i=='p':
            cnt = cnt + 1
        elif i=='P':
            cnt = cnt + 1
        elif i=='y':
            cnt = cnt - 1
        elif i=='Y':
            cnt = cnt - 1
        else :
            pass
    print(cnt)
    if cnt == 50:
        return True
    else:
        return False