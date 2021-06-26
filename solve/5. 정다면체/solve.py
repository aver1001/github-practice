'''

두 개의 정 N면체와 정 M면체의 두 개의 주사위를 던져서
나올 수 있는 눈의 합 중 가장 확 률이 높은 숫자를 출력하는 프로그램을 작성하세요.
정답이 여러 개일 경우 오름차순으로 출력합니다.
'''
import sys


for sn in range (1,6):
    sn = str(sn)
    input_file_name = 'in' + sn +'.txt'
    output_file_name = 'out' + sn +'.txt'
    
    sys.stdin = open (input_file_name, "rt")
    output_file = open(output_file_name, "rt")

#################################################################
    ## n은 갯수, k번째 큰 수
    n, m = map(int,input().split())

    result = list()
    result_2 = list()
    result_3 = list()

    ## 가능한 합 
    for i in range (1,n+1):
        for j in range (1,m+1):
            result.append(i+j)

    #확률 
    for i in range (1,n+m+1):
        result_2.append(result.count(i))

    max_result=max(result_2)

    for i in range (0,n+m):
        if result_2[i] == max_result:
            print(i+1,end=" ")
#################################################################
    print("\n"+output_file.read()+"\n####################\n")

    


