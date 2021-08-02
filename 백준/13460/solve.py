'''


'''
import sys
import time

xpos = [0,-1,0,1]
ypos =[-1,0,1,0]
def DFS (rx,ry,bx,by,count):
    global Min
    print(rx,ry,bx,by,count)

    if count > 10:
        return

    if a[rx][ry] == 'O':
        print("GOAL",count)
        if Min > count :
            Min = count
        return

    for i in range (4):
        ## 좌 상 우 하
        # red는 .이거나 0이고 blue는 0이 아닐경우
        if (a[rx+xpos[i]][ry+ypos[i]] == '.' or a[rx+xpos[i]][ry+ypos[i]] == 'O' )and a[bx+xpos[i]][by+ypos[i]] != '0' :
            if a[bx+xpos[i]][by+ypos[i]] =='#':
                DFS(rx+xpos[i],ry+ypos[i],bx,by,count+1)
            else:
                DFS(rx+xpos[i],ry+ypos[i],bx+xpos[i],by+ypos[i],count+1)

    
start = time.time()
for sn in range (2,3):
    sn = str(sn)
    input_file_name = 'in' + sn +'.txt'
    output_file_name = 'out' + sn +'.txt'
    
    sys.stdin = open (input_file_name, "rt",encoding = 'utf-8')
    output_file = open(output_file_name, "rt",encoding = 'utf-8')

#################################################################
    n,m = map(int,input().split(' '))
    a = list()
    global Min
    Min = 9999
    for i in range (m):
        a.append(list(input()))
    

    for i in range (m):
        for j in range (n):
            if a[i][j] ==  "R":
                rx,ry = i,j

    for i in range (m):
        for j in range (n):
            if a[i][j] ==  "B":
                bx,by = i,j         
    print("R",rx,ry,"B",bx,by)
    DFS(rx,ry,bx,by,0)
    print(Min)

    

#################################################################
    print("\n"+output_file.read()+"\n####################\n")
end = time.time()
print('time elapsed', end - start)

    


