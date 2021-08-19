def solution(n,a,b):
    cnt = 0
    while(a != b):
        a = (a+1)//2
        b = (b+1)//2
        cnt+=1

    return cnt

N = 8
A = 4
B = 7
result = 3

solution(N,A,B)

## N  참가자 수
## A,B 경쟁자 
