def solution(n, build_frame):
    ## n  =>  n x n
    ## build_frame(x,y,a,b)  => x,y 좌표 a = 0 기둥, a = 1 보, b = 0 삭제 , b = 1 설치
    ## return (x,y,a)  => x,y 교차점 좌표, a = 0 기둥, a = 1 보
    n = n+2
    column = [[0]*n for _ in range (n)]
    cover = [[0]*n for _ in range (n)]
    cnt = 0
    for y,x,a,b in build_frame:
        
        cnt += 1
        if a == 0: aa = '기둥'
        else: aa = '보'
        if b == 0: bb = '삭제'
        else: bb = '설치'
        print('(',x,',',y,')',aa,bb,"  ",cnt)
        
        # 기둥
        # 기둥은 바닥 위에 있거나 보의 한쪽 끝 부분 위에 있거나, 또는 다른 기둥 위에 있어야 합니다.
        if 0 <= x < n-1 and 0 <= y < n-1:
            if a == 0:
                # 설치
                if b == 1:
                    if x == 0 or (0<y<n and ((cover[x][y-1]== 1 and cover[x][y+1] == 0) or (cover[x][y-1] == 0 and cover[x][y+1] == 1))) or (x > 0 and column[x-1][y] == 1):
                        print(x,y,"기둥을 설치합니다.")
                        column[x][y] = 1
                        column[x+1][y] = 1
                # 삭제
                elif b == 0:
                    # 보가 없거나 기둥이 없어야함.
                    if cover[x+1][y] == 0 and column[x+2][y] == 0:
                        print(x,y,"기둥을 삭제합니다.")
                        column[x+1][y] = 0
                        ## 밑에도 기둥이 잇을경우 그좌표는 놔두고
                        ## 아닐경우 삭제
                        if column[x-1][y] != 1:
                            column[x][y] = 0
                
            # 보
            # 보는 한쪽 끝 부분이 기둥 위에 있거나, 또는 양쪽 끝 부분이 다른 보와 동시에 연결되어 있어야 합니다.
            elif a== 1:
                # 설치
                if b == 1:
                    if (column[x][y] == 1 or column[x][y+1] == 1) or (cover[x][y-1] == 1 and cover[x][y+1]):
                        print(x,y,"보를 설치합니다.")
                        cover[x][y] = 1
                        cover[x][y+1] = 1
                # 삭제
                elif b == 0:
                    ## 양쪽다 기둥이 없거나 양쪽다 보가 없을경우
                    if (column[x][y] == 0 and column[x][y+1] == 0) or (cover[x][y] == 0 and cover[x][y+1] == 0):
                        print(x,y,"보를 삭제합니다.")

        print("기둥               ","보")
        for a,b in zip(column,cover):print(a,"   ",b)
        
    
    
solution(5,[[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]])

