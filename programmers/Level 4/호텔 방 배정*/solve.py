def find(number, room):
    if number not in room:
        room[number] = number + 1
        return number
    
    empty = find(room[number], room)
    room[number] = empty + 1
    return empty
    
def solution(k, room_number):
    answer = []
    
    dic = {}
    
    for i in room_number:
        print(i)
        num = find(i, dic)
        print(dic)
        answer.append(num)
    
    return answer


solution(10,[1,1,1,1,1,1]) #[1,3,4,2,5,6]
