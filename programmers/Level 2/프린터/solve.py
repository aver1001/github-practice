def solution(priorities, location):
    
    a = list(enumerate(priorities))
    cnt = 0 
    while a:
        print(a)
        temp = a.pop(0)
        if temp[1] >= max(a, key = lambda x: x[1])[1]:
            cnt += 1
            if temp[0] == location:
                return cnt
        else:
            a.append(temp)

priorities = [1, 1, 9, 1, 1, 1]
location = 0
answer = 1

print(solution(priorities,location))
