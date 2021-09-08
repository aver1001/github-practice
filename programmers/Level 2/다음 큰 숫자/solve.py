def solution(n):
    temp = bin(n).count('1')
    while(1):
        n += 1
        if bin(n).count('1') == temp:
            return n

print(solution(78))
