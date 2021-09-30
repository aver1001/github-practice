result = []

def hanoi(n,start,end,mid):
    global result
    
    if n == 1:
        result.append([start,end])
    else:
        hanoi(n-1, start, mid, end)
        result.append([start,end])
        print([start,end])
        hanoi(n-1, mid, end, start)

    return result

def solution(n):
    global result

    hanoi(n,1,3,2)

    print(result)


solution(6)
