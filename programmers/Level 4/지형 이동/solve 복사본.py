from collections import deque
import heapq
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
    board = []
    for x in range (N+1):
        for y in range (N+1):
            if table[x+1][y+1] == 0:
                diffrence_height = []
                cnt += 1
                queue = deque([[x,y]])
                while queue:
                    while queue:
                        a,b = queue.popleft()
                        table[a+1][b+1] = cnt
                        for ax,ay in move:
                            if  table[a+ax+1][b+ay+1] == 0:
                                value = abs(land[a][b] - land[a+ax][b+ay])
                                ## 갈수 있을경우 
                                if value <= height:
                                    table[a+ax+1][b+ay+1] = cnt
                                    queue.append([a+ax,b+ay])
                                # 갈수 없을경우
                                else:
                                    heapq.heappush(board,[value,a,b,a+ax,b+ay])
                    while board:
                        k = heapq.heappop(board)
                        if table[k[3]+1][k[4]+1] == 0:
                            answer += k[0]
                            queue.append([k[3],k[4]])
                            break

    return answer


    

solution([[1, 4, 8, 10], [5, 5, 5, 5], [10, 10, 10, 10], [10, 10, 10, 20]],3)
#solution([[10, 11, 10, 11], [2, 21, 20, 10], [1, 20, 21, 11], [2, 1, 2, 1]],1)
