from collections import deque
from itertools import permutations
Board = []
def bfs(r,c,cost):
    queue = deque([[r,c,0]])
    while queue:
        x,y,v = queue.popleft()
        if x == 2 and y == 3:
            break
        for ax,ay in [[-1,0],[1,0],[0,-1],[0,+1]]:
            
            while(True):
                if 0 <= x + ax+1 <= 3 and  0<= y + ay+1 <= 3 and Board[x+ax+1][y+ay+1] == 0:
                    ax += 1
                    ay += 1
                else:
                    queue.append([x+ax,y+ay,v+1])
                    break
    return v+cost
def solution(board, r, c):
    global Board
    Board = board
    
    for i in board: print(i) 
    ## 입력크기 board 는 4*4 이므로 복잡도는 신경 쓰지않고 풀어보자
    
    ## 두 좌표 사이의 이동 횟수를 구하는 함수를 만들자!
    ## 2 (1,0) 2 (2,3)


    print(bfs(1,0,0))

    ## 카드 제거할 순서들을 모아보자
    Max = 0
    table = {}
    for i in range (4):
        for j in range (4):
            num = board[i][j]
            if num > Max:
                Max = num
            if num != 0:
                if num in table:
                    table[num].append([i,j])
                else:
                    table[num] = [[i,j]]
    print(table)
    #for course in (list(permutations([i for i in range (1,Max+1)], Max))):

            
        
    
            
            

    
solution([[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]],1,0)
