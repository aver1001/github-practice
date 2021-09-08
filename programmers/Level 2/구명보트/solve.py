def solution(people, limit):
    people.sort()
    cnt = 0
    while people :
        print(people)
        heavy = people.pop()
        for i in range(len(people)):
            if heavy + people[i] > limit:
                break
        if len(people) == 0:
            cnt += 1
            break
            
        if i == 0:
            if len(people) == 1:
                light = people.pop(i-1)
                if light + heavy <= limit:
                    cnt +=1
                else:
                    cnt +=2
            else:
                cnt += 1
        else:
            people.pop(i-1)
            cnt += 1 
        print(cnt)
    return cnt
            



print(solution([40, 50, 60, 90],100))
