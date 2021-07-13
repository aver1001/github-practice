'''
N*N의 격자판이 주어지면
각 행의 합, 각 열의 합, 두 대각선의 합중 가장 큰 합을 출력합니다.

'''
import sys
import time


start = time.time()
for sn in range (5,6):
    sn = str(sn)
    input_file_name = 'in' + sn +'.txt'
    output_file_name = 'out' + sn +'.txt'
    
    sys.stdin = open (input_file_name, "rt",encoding = 'utf-8')
    output_file = open(output_file_name, "rt",encoding = 'utf-8')

#################################################################
    ## n = 격자판 n x n
    n= int(input())
    a = list()
    result = list()
    temp_1,temp_2 = 0,0
    for i in range (n):
        in_list = list(map(int,input().split()))
        a.append(in_list)
    for i in range (n):
        result.append(sum(a[i][:]))
        result.append(sum(a[:][i]))
        temp_1 += a[i][i]
        temp_2 += a[i][n-i-1]
    result.append(temp_1)
    result.append(temp_2)

    '''
    in_5 틀린 값이 나오는데 왜그런지 모르겠음.
    '''
#################################################################
    print(max(result))
#################################################################
    print("\n"+output_file.read()+"\n####################\n")
end = time.time()
print('time elapsed', end - start)

    


