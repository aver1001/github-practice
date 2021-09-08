

def solution(n, times):
    lt,rt = 1, n*times[0]
    answer = 0
    while(lt <= rt):
        pt = (lt+rt)//2
        temp = 0
        for i in times:
            temp += pt // i 
        if temp < n:
            answer = pt
            lt = pt +1
        elif temp >= n:
            rt = pt -1

    return answer
    

solution(6,[7,10])        
        
