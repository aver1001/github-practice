'''
지도 정보가 N*N 격자판에 주어집니다.
각 격자에는 그 지역의 높이가 쓰여있습니다.
각 격자 판의 숫자 중 자신의 상하좌우 숫자보다 큰 숫자는 봉우리 지역입니다.
봉우리 지역이 몇 개 있는 지 알아내는 프로그램을 작성하세요.
격자의 가장자리는 0으로 초기화 되었다고 가정한다.
만약 N=5 이고, 격자판의 숫자가 다음과 같다면 봉우리의 개수는 10개입니다.

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

    ## 지도생성
    a = [[0]*(n+2)]
    for i in range (n):
        temp = list(map(int,input().split()))
        temp.insert(0,0)
        temp.append(0)
        a.append(temp)
            
    temp = [0]*(n+2)
    a.append(temp)
    

    ## 봉우리 계산 
    cnt = 0
    for i in range(1,n+1):
        for j in range(1,n+1):
            #print(a[i][j]," : " ,a[i-1][j],a[i][j-1],a[i+1][j],a[i][j+1])
            if a[i][j] > a[i+1][j] and a[i][j] > a[i-1][j] and a[i][j] > a[i][j+1]and a[i][j] > a[i][j-1] :
               cnt +=1
    '''
    for i in range (0,n+2):
        for j in range(0,n+2):
            print(a[i][j])
    '''
    
#################################################################
    print(cnt)
#################################################################
    print("\n"+output_file.read()+"\n####################\n")
end = time.time()
print('time elapsed', end - start)

    


