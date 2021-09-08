

def solution(n):
    cnt = 0
    for i in range(1, n + 1):
        if n % i == 0 and i % 2 == 1:
            cnt +=1

    return cnt

print(solution(15))
