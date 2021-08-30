def solution(n):
    F = [0 for _ in range (n+2)]
    F[0] = 0
    F[1] = 1
    for i in range(2,n+1):
        F[i] = F[i-1] + F[i-2]
        print(F,i)
    return F[n]
        


print(solution(3))

## 배열을 사용하지 않고 그냥 정수를 이용해서 메모리 낭비를 하지 않을 수 있음.
