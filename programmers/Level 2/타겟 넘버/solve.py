  
def solution(numbers, target):
    
    global cnt
    cnt = 0
    numbers = numbers
    target = target

    DFS(0,0,numbers,target) 
    
    return cnt


def DFS(v,num,numbers,target):
    
    global cnt
    
    if v == len(numbers):
        if target == num:
            cnt += 1
        return
    
    DFS(v+1, num + numbers[v],numbers,target)
    DFS(v+1, num - numbers[v],numbers,target)



