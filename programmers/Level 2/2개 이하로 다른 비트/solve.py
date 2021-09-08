def solution(numbers):
    answer = []
    for i in numbers:
        if i % 2 == 0:
            temp = i+1
        else:
            temp = '0'+bin(i)[2:]
            index = temp.rfind('0')
            temp = list(temp)
            temp[index] = '1'
            temp[index+1] = '0'
            temp = int("".join(temp),2)
        answer.append(temp)
            
    return answer





