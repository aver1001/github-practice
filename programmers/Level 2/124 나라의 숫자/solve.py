def solution(n):
    
    answer = ''
    while(True):
        if n == 0:
            break

        na = n % 3
        n = n // 3
        
        if na == 0:
            n -=1
            answer = '4' + answer
        elif na == 1:
            answer = '1' + answer
        elif na == 2:
            answer = '2' + answer

        
    return answer


for i in range (0,30):
    print(i, " => ",solution(i))

