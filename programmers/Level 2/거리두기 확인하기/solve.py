def DFS(v,place,x,y):
    global cnt,Fx,Fy
    xPos = [1,0,-1,0]
    yPos = [0,1,0,-1]
    
    if v == 1:
        if place[x][y] == 'P':
            cnt += 1
        if place[x][y] == 'X':
            return
    if v == 2:
        if place[x][y] == 'P':
            cnt += 1
        return

    for i in range (4):
        if Fx == x+xPos[i] and Fy == y+yPos[i]:
            continue
        if x+xPos[i]>=0 and x+xPos[i] <= 4 and y+yPos[i]>=0 and y+yPos[i]<=4:
            DFS(v+1,place,x+xPos[i],y+yPos[i])

    
    

def solution(places):
    global cnt,Fx, Fy
    answer = []
    for i in places:
        cnt = 0
        for j in range (5):
            for k in range (5):
                if i[j][k] == 'P':
                    Fx = j
                    Fy = k
                    DFS(0,i,j,k)
        if cnt == 0:
            answer.append(1)
        else:
            answer.append(0)
    return answer

places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]

solution(places)

# O = 빈테이블
# P = 응시자
# X = 파티션 
