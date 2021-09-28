'''
정확성 만점
효율성 50점

1씩 빼는것이 아닌 가장큰거를 두번쨰로 맞춰주면서 뺴야겠음.
'''


def solution(n, works):
    
    works.sort(reverse = True)
    N = len(works)
    pt = 0
    while (n != 0):
        if pt == 0:
            if works[pt] == 0:
                return 0
            check = works[0]-1
            n -= 1
            works[0] -= 1
        else:
            if works[pt] >= check:
                works[pt] -= 1
                n -= 1       
        pt += 1
        
        if pt == N:
            pt = 0
        
        
    answer = 0
    for i in works:
        answer += i*i
        
    return(answer)
