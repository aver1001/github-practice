def check(num,arr,floor):
    temp = []
    for idx,q in enumerate(arr[:floor+1]):
        temp.append(idx+q+1)
    if( num not in arr )and (num not in temp):
        return True
    return False


def N_Queen(arr,floor):
    global cnt
    if len(arr) <= floor:
        cnt += 1
        return
    
    if floor == 0:
        for i in range (len(arr)):
            arr[floor] = i
            N_Queen(arr,floor+1)
            arr[floor] = -1
    else:
        for i in range (len(arr)):
            temp = arr[floor-1]
            ## 대각선 경우 추가 해야함
            if check(i,arr,floor) :
                arr[floor] = i
                N_Queen(arr,floor+1)
                arr[floor] = -1
            
        

def solution(n):
    global cnt
    cnt = 0
    N_Queen([-1]*(n),0)
    return cnt

solution(4)
