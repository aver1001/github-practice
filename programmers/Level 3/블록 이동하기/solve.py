import deque

def solution(board):
    N = len(board)
    direction = [[1,0],[0,1],[-1,0],[0,-1]]
    
    ## 계산하기 쉽게 벽으로 둘려쳐준다
    new_board = [[1] * (N+2) for _ in range(N+2)]
    for i in range (1,N+1):
        for j in range (1,N+1):
            new_board[i][j] = board[i-1][j-1]

    queue = deque([1,1,1,2,0])
    #for i in new_board: print(i)
    ## 가능 동선
    ## 상하좌우 이동
    ## 4방향 회전

    while queue:
        x1,y1,x2,y2,cnt = queue.popleft()
        ## 현재 가로방향일 경우
        if x1 == x2:
            for i in
        ## 현재 세로방향일 경우
        else:


        
    

solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]])
