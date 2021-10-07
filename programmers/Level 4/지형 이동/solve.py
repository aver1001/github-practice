from collections import deque

def solution(land, height):
    N = len(land)
    table = [[0]*(N+2) for _ in range (N+2)]
    for i in range (N+2):
        for j in range (N+2):
            if i == 0 or i == N+1 or j == 0 or j == N+1:
                table[i][j] = -1

    move = [[1,0],[0,1],[-1,0],[0,-1]]
    cnt = 0

    answer = 0
    
    for x in range (N+1):
        for y in range (N+1):
            if table[x+1][y+1] == 0:
                diffrence_height = []
                cnt += 1
                queue = deque([[x,y]])
                while queue:
                    a,b = queue.popleft()
                    table[a+1][b+1] = cnt
                    for ax,ay in move:
                        if  table[a+ax+1][b+ay+1] == 0:
                            if abs(land[a][b] - land[a+ax][b+ay]) <= height:
                                table[a+ax+1][b+ay+1] = cnt
                                queue.append([a+ax,b+ay])
                            else:
                                diffrence_height.append([[a+ax,b+ay],abs(land[a][b] - land[a+ax][b+ay])])
                
                if len(diffrence_height) == 0:
                    min_height = 0
                else:
                    diffrence_height.sort(key = lambda x:x[1])
                    print(diffrence_height)
                    for (i,j),price in diffrence_height:
                        if table[i+1][j+1] == 0:
                            min_height = price
                            break
                print(cnt,min_height)
                answer += min_height
    for i in table:print(i)
    return answer


    

#solution([[1, 4, 8, 10], [5, 5, 5, 5], [10, 10, 10, 10], [10, 10, 10, 20]],3)
solution([[10, 11, 10, 11], [2, 21, 20, 10], [1, 20, 21, 11], [2, 1, 2, 1]],1)
