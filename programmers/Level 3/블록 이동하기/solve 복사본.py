from collections import deque

def solution(board):
    N = len(board)
    direction = [[1,0],[0,1],[-1,0],[0,-1]]
    
    ## 계산하기 쉽게 벽으로 둘려쳐준다
    new_board = [[1] * (N+2) for _ in range(N+2)]
    for i in range (1,N+1):
        for j in range (1,N+1):
            new_board[i][j] = board[i-1][j-1]


    for i in new_board : print(i)
    queue = deque([[1,1,1,2,0]])

    while queue:
        x1,y1,x2,y2,cnt = queue.popleft()

        ## 정지조건
        if (x1 == N and y1 == N )or (x2 == N and y2 == N):
            print(cnt)
            return cnt
    
        #상
        if new_board[x1-1][y1] == 0 and new_board[x2-1][y2] == 0:
            queue.append([x1-1,y1,x2-1,y2,cnt+1])
        #하
        if new_board[x1+1][y1] == 0 and new_board[x2+1][y2] == 0:
            queue.append([x1+1,y1,x2+1,y2,cnt+1])
        #좌
        if new_board[x1][y1-1] == 0 and new_board[x2][y2-1] == 0:
            queue.append([x1,y1-1,x2,y2-1,cnt+1])
        #우
        if new_board[x1][y1+1] == 0 and new_board[x2][y2+1] == 0:
            queue.append([x1,y1+1,x2,y2+1,cnt+1])

        #회전

        #가로
        if x1 == x2:
            # ↳
            if new_board[x1+1][y1] == 0 and new_board[x2+1][y2] == 0:
                queue.append([x2,y2,x2+1,y2,cnt+1])
            # ↲
            if new_board[x2+1][y2] == 0 and new_board[x1+1][y1] == 0:
                queue.append([x1,y1,x1+1,y1,cnt+1])
            # ↱
            if new_board[x1-1][y1] == 0 and new_board[x2-1][y2] == 0:
                queue.append([x2-1,y2,x2,y2,cnt+1])
            # ↰
            if new_board[x2-1][y2] == 0 and new_board[x1-1][y1] == 0:
                queue.append([x1-1,y1,x1,y1,cnt+1])

        #세로
        elif y1 == y2:
            #⬎
            if new_board[x1][y1+1] == 0 and new_board[x2][y2+1] == 0:
                queue.append([x2,y2,x2,y2+1,cnt+1])
            #⬏
            if new_board[x2][y2+1] == 0 and new_board[x1][y1+1] == 0:
                queue.append([x1,y1,x1,y1+1,cnt+1])
            #⬐
            if new_board[x1][y1-1] == 0 and new_board[x2][y2-1] == 0:
                queue.append([x2,y2-1,x2,y2,cnt+1])
            #⬑
            if new_board[x2][y2-1] == 0 and new_board[x1][y1-1] == 0:
                queue.append([x1,y1-1,x1,y1,cnt+1])
        
    

solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]])
