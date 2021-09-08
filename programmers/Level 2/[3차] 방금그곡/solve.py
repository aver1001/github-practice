def change(a):
    for before, after in [['A#','a'],['G#','g'],['F#','f'],['D#','d'],['C#','c']]:
        a = a.replace(before,after)
    return a

def solution(m, musicinfos):
    Max = 0
    answer = None
    for i in musicinfos:
        infos = i.split(',')
        shour,smin = map(int,infos[0].split(':'))
        ehour,emin = map(int,infos[1].split(':'))
        name = infos[2]
        m = change(m)
        code = change(infos[3])
        pt = 0
        temp = ''
        for j in range((ehour-shour)*60 + emin - smin):
            temp += code[pt]
            pt += 1
            if pt == len(code):
                pt = 0
                
        if m in temp:
            if (ehour-shour)*60 + emin - smin > Max:
                answer = name

    if answer == None:
        return '(None)'
    else:
        return answer

print(solution("ABC",["12:00,12:14,HELLO,CDEFGAB", "13:00,13:14,WORLD,ABCDEF"]))
