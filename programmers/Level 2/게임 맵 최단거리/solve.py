def solution(maps):
    dd = [[1,0],[0,1],[-1,0],[0,-1]]
    ## 가로세로를 구해준다
    y = len(maps)
    x = len(maps[0])
    check = [[-1 for i in range(x)]for i in range (y)]
    check[0][0] = 1
    queue = []
    queue.append([0,0])
    while queue :
        b,a = queue.pop(0)
        
        for i in dd:
            dy = i[0]+b
            dx = i[1]+a

            if 0 <= dx < x and 0 <= dy < y:

                if maps [dy][dx] == 1 and check[dy][dx] == -1:
                    check[dy][dx] = check[b][a] + 1
                    queue.append([dy,dx])
                
    return check[-1][-1] 


maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]
answer = 11
print(solution(maps))

