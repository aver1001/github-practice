'''
스도쿠는 매우 간단한 숫자 퍼즐이다.9×9 크기의 보드가 있을 때,
각 행과 각 열, 그리고 9 개의 3×3 크기의 보드에 1부터 9까지의 숫자가
중복 없이 나타나도록 보드를 채우면 된다.

완성된 9×9 크기의 수도쿠가 주어지면
정확하게 풀었으면 “YES", 잘 못 풀었으면 ”NO"를 출 력하는 프로그램을 작성하세요.


'''
import sys
import time

start = time.time()
for sn in range (1,6):
    sn = str(sn)
    input_file_name = 'in' + sn +'.txt'
    output_file_name = 'out' + sn +'.txt'
    
    sys.stdin = open (input_file_name, "rt",encoding = 'utf-8')
    output_file = open(output_file_name, "rt",encoding = 'utf-8')

#################################################################
    a = list()
    for i in range (9):
        a.append(list(map(int,input().split())))

    check = 0
    for i in range (9):   
        for j in range (1,10):
            try:
                a[i][:].index(j) #가로
                a[:][i].index(j) #세로
            except:
                #print("가로세로")
                check = 1
                break
            
        if check == 1:
            break

    if check != 1:
        x,y = 0,0
        for x in range (0,9,3):
            for y in range(0,9,3):
                temp = list()
                for i in range (3):
                    for j in range (3):
                        #print(x+i,y+j)
                        temp.append(a[x+i][y+j])
                #print(temp)
                for k in range(1,10):
                    try:
                        temp.index(k)
                    except:
                        #print("정사각형 ")
                        check =1

    if check ==1:
        print("NO")
    else :
        print("YES")
    
#################################################################
#################################################################
    print("\n"+output_file.read()+"\n####################\n")
end = time.time()
print('time elapsed', end - start)

    


