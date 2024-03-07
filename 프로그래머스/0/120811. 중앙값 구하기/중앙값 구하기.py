def solution(array):
    arraylist = list(array)
    arraylist.sort()
    answer = arraylist[int(len(arraylist)/2)]
    return answer