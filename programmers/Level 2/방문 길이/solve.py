def solution(dirs):
    x = 0
    y = 0
    beforeRoad = set()
    cnt = 0
    for i in dirs:
        print(i,end = ' => ')
        temp = str(x) + str(y)
        #Up
        if i == 'U' and y != 5:
            y += 1
        #Down
        elif i == 'D' and y != -5:
            y -= 1
        #Right
        elif i == 'R' and x != 5:
            x += 1
        #Left
        elif i == 'L' and x != -5:
            x -= 1
        else :
            print(x,y,cnt)
            continue
        #초행길일 경우 
        if temp+str(x)+str(y) not in beforeRoad:
            beforeRoad.add(temp+str(x)+str(y))
            beforeRoad.add(str(x)+str(y)+temp)
            cnt += 1
        
        print(x,y,cnt)

solution("LULLLLLLU")
