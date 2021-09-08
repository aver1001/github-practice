def printBoard(a):
    for i in a:print(i)
    print()

def solution(m, n, board):
    board = list(map(list,board))
    delete = 0
    while (1):
        check = [[0 for _ in range(n)] for _ in range(m)]
        
        for i in range (m-1):
            for j in range (n-1):
                if board[i][j] == board[i+1][j] == board[i][j+1] == board[i+1][j+1] and board[i][j] != 0: #and board[i][j] == board[i][j+1]:
                    check[i][j] = 1
                    check[i+1][j] = 1
                    check[i][j+1] = 1
                    check[i+1][j+1] = 1
            
        printBoard(check)
        printBoard(board)
        deleteBefore = delete
        for i in range(m):
            for j in range (n):
                if check[i][j] == 1:
                    board[i][j] = 0
                    delete +=1
        if deleteBefore == delete:
            return delete
        printBoard(board)
        for i in range (1,m):
            for j in range (n):
                if board[i][j] == 0:
                    count = 0
                    while(1):
                        if i-count-1 <0:
                            break
                        board[i-count][j] = board[i-count-1][j]
                        board[i-count-1][j] = 0
                        count += 1
                        
        printBoard(board)       
                
    printBoard(board)
    



print(solution(7,2,["AA", "BB", "AA", "BB", "ZZ", "ZZ", "CC"]))
