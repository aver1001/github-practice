def solution(s):
    answer = ''
    check = 0
    for i in s:
        if check == 0:
            answer += i.upper()
            check = 1
        else:
            answer += i.lower()
        if i == ' ':
            check = 0
    return answer
        
print(solution("3people unFollowed me"))

