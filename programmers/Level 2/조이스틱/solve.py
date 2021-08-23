def solution(name):

    ## 이름변경 횟수
    updown = 0
    for i in name:
        updown += min(abs(ord(i)-ord('A')),91 - ord(i))

    ## 좌우 이동 횟수
    name = list(name)
    pt = 0
    cnt = 0
    while (True):
        name[pt] = 'A'
        lt,rt = pt,pt
        if all('A' == i for i in name):
            break
        while (True):
            cnt += 1
            rt += 1
            lt -= 1
            if name[rt] != 'A':
                pt = rt
                break
            if name[lt] != 'A':
                pt = lt
                break

    return updown+cnt

a = solution("JEROEN")

    


