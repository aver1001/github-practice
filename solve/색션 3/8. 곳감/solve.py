'''
현수는 곳감을 만들기 위해 감을 깍아 마당에 말리고 있습니다.
현수의 마당은 N*N 격자판으 로 이루어져 있으며,
현수는 각 격자단위로 말리는 감의 수를 정합니다.
그런데 해의 위치에 따라 특정위치의 감은 잘 마르지 않습니다.
그래서 현수는 격자의 행을 기준으로
왼쪽, 또는 오른쪽으로 회전시켜 위치를 변경해 모든 감이 잘 마르게 합니다.
만약 회전명령 정보가 2 0 3이면
2번째 행을 왼쪽으로 3만큼 회전시키는 명령 입니다.
M개의 회전명령을 실행하고 난 후 마당의 모래시계 모양의 영역에는
감 이 총 몇 개가 있는지 출력하는 프로그램을 작성하세요.

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
    ## n =
    n = int(input())
    a = list()
    for i in range (n):
        a.append(list(map(int,input().split())))
    m = int(input())
    b = list()
    for i in range (m):
        x,y,z = map(int,input().split())
        # 한바퀴 이상 돌 경우
        if z >= n: 
            z = z-n
        #왼쪽 이동경우
        if y == 0:
            temp = a[x-1][:z]
            del(a[x-1][:z])
            a[x-1].extend(temp)
        #오른쪽 이동경우
        elif y == 1:
            temp = a[x-1][:n-z]
            del(a[x-1][:n-z])
            a[x-1].extend(temp)


    #모리시계모양 합 구하기.
    cnt=1
    result = 0
    lt,rt = 0,n
    for i in range (n):
        if i == n//2 :
            cnt =-1
            rt,lt == n//2,n//2
        result += sum(a[i][lt:rt])
        lt += cnt
        rt -= cnt
            
#################################################################
    print(result)
#################################################################
    print("\n"+output_file.read()+"\n####################\n")
end = time.time()
print('time elapsed', end - start)

    


