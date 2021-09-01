def zin(num,zin):
    result = ''
    while(num > zin-1):
        temp = num % zin
        if temp >= 10:
            result = chr(65 + temp - 10) + result
        else:
            result = str(temp) + result
        num //= zin

    if num >= 10:
        return chr(65 + num - 10) + result
    else:
        return str(num) + result
        

def solution(n, t, m, p):
    cnt = 0
    temp = ''
    while(1):
        temp += zin(cnt,n)
        cnt += 1
        if len(temp) >= t*m:
            break
    answer = ''
    p -= 1
    while(len(answer) != t):
        answer += temp[p]
        p += m
    return(answer)
        

    


solution(2,4,2,1)
