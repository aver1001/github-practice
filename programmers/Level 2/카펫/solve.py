def solution(brown, yellow):
    for i in range (1,yellow+1):
        if i % 1 == 0 and (i+yellow/i)*2+4 == brown:
                return [max(int(yellow/i+2),i+2),min(int(yellow/i+2),i+2)]


brown = 8
yellow = 1
answer = [4,3]

print(solution(brown,yellow))
