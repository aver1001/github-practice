def solution(n):
    
    fac = [0]*29
    fac[1] = 1
    fac[2] = 2
    for i in range (3,29):
        fac[i] = fac[i-1]*i
    
    return fac[2*n] / (fac[n+1] *fac[n])

    ## 카탈린의 수
