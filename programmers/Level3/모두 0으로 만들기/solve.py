from collections import deque

def solution(a, edges):
    if sum(a) != 0:
        return -1
    
    table = {}
    
    for x,y in edges:
        if x not in table:
            table[x] = [y]
        else:
            table[x].append(y)
        if y not in table:
            table[y] = [x]
        else:
            table[y].append(x)


    queue = deque([0])
    tabble = {}
    check = [0 for _ in range (len(a))]
    check[0] = -1
    while queue :
        idx = queue.popleft()
        for i in table[idx]:
            if check[i] != -1:
                if idx not in tabble:
                    tabble[idx] = [i]
                else:
                    tabble[idx].append(i)
                queue.append(i)
                check[i] = -1


    
    answer = 0
    temp = list(tabble.items())
    temp.reverse()
    for up,down in temp:
        for idx in down:
            if a[idx] != 0:
                print(idx,up)
                temp = a[idx]
                a[idx] = 0
                a[up] += temp
                answer += abs(temp)
                print(a,answer)
            
    print(answer)

solution([-5,0,2,1,2],
         [[0,1],[3,4],[2,3],[0,3]])
