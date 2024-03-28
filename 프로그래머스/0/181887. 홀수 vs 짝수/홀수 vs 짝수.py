def solution(num_list):
    answer = 0
    oddSum = 0
    evenSum = 0 
    for i in range(len(num_list)):
        if i % 2 :
            evenSum += num_list[i]
        else:
            oddSum += num_list[i]
    answer = max(oddSum,evenSum)
            
    return answer