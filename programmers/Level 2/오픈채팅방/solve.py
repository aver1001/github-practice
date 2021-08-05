def solution(record):
    
    userName = dict()
    answer = []
    
    for i in range (len(record)):
        record[i] = record[i].split(' ')
        if len(record[i]) == 3:
            userName[record[i][1]] = record[i][2]

    for i in record:
        if i[0] == 'Enter':
            answer.append(userName[i[1]]+'님이 들어왔습니다.')
        elif i[0] == 'Leave':
            answer.append(userName[i[1]]+'님이 나갔습니다.')
    return answer



record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(record))
