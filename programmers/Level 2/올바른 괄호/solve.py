def solution(s):
    cnt = 0
    for i in s:
        if cnt < 0 :
            return False
        if i == '(':
            cnt += 1
        else:
            cnt -= 1

    if cnt == 0:
        return True
    else:
        return False
            


print(solution("(())()"))
