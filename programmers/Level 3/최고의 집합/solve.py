def solution(n, s):
    

    
    mok = s // n
    na = s % n
    if mok == 0:
        return [-1]

    answer = [mok]*n

    for i in range (na):
        answer[i] += 1
    answer.reverse()
    print(answer)
    
    return answer



solution (2,1) ## [4,5]
