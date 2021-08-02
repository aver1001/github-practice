'''


'''
import sys
import time
import queue

xpos = [-1,1,0,0]
ypos = [0,0,-1,1]
name = ['상','하','좌','우']

def DFS (rx,ry,bx,by):
    queue =list()
    queue.append([rx,ry,bx,by,1])

    while(queue):
        rx,ry,bx,by,count = queue.pop(0)

        if count > 10:
            print(-1)
            return
        
        if a[bx][by] == 'O':
            continue
        
        for i in range (4):
            check = 0
            #print(name[i])
            Trx = rx
            Try = ry
            Tbx = bx
            Tby = by
            while(True):
                if a[Trx + xpos[i]][Try + ypos[i]] == 'O':
                    check += 1
                    break
                if a[Trx + xpos[i]][Try + ypos[i]] == '#':
                    break
                Trx += xpos[i]
                Try += ypos[i]

            #print("#######################")
            while(True):
                if a[Tbx + xpos[i]][Tby + ypos[i]] == 'O':
                    check += 1
                    break
                if a[Tbx + xpos[i]][Tby + ypos[i]] == '#':
                    break
                Tbx += xpos[i]
                Tby += ypos[i]
            if Trx == Tbx and Try ==  Tby:
                if (abs(rx - Trx)+abs(ry - Try)) < (abs(bx - Tbx)+abs(by - Tby)):
                    Tbx -= xpos[i]
                    Tby -= ypos[i]
                else:
                    Trx -= xpos[i]
                    Try -= ypos[i]
            if check == 1:
                print("Find !! :",count)
                return
            #print("Red :",Trx,Try,"  Blue :",Tbx,Tby,"   Count :",count)
            queue.append([Trx,Try,Tbx,Tby,count+1])
        
        
        
    

start = time.time()
for sn in range (1,8):
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
    for i in range (n):
        a.append(list(input()))
    

    for i in range (n):
        for j in range (m):
            if a[i][j] ==  "R":
                rx,ry = i,j

    for i in range (n):
        for j in range (m):
            if a[i][j] ==  "B":
                bx,by = i,j

    for i in a:
        print(i)
    print("R",rx,ry,"B",bx,by)
    DFS(rx,ry,bx,by)

    

#################################################################
    print("\n"+output_file.read()+"\n####################\n")
end = time.time()
print('time elapsed', end - start)

    


