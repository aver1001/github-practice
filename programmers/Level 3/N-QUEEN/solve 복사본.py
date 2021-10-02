def check(num,arr,floor):
    #print('Check!',arr,floor,'index','put',num)
    for i in range (floor):
        if arr[i] == num or arr[i]+(floor-i) == num or arr[i]-(floor-i) == num :
            #print('False',arr[i],'==',floor,'or',arr[i]+i+1,'==',floor)
            return False
    #print('True')
    return True



def N_Queen(arr,floor):
    global cnt
    if len(arr) == floor :
        cnt += 1
        return
        

    if floor == 0:
        for i in range (len(arr)):
            arr[0] = i
            N_Queen(arr,floor+1)
        arr[0] = -1
    else:
        for i in range (len(arr)):
            if check(i,arr,floor):
                arr[floor] = i
                N_Queen(arr,floor+1)

                
        

            
        

def solution(n):
    global cnt
    cnt = 0
    N_Queen([-1]*(n),0)
    return cnt

solution(4)
