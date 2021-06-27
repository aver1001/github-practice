'''

현수는 1부터 100사이의 자연수가 적힌 N장의 카드를 가지고 있습니다.
같은 숫자의 카드가 여러장 있을 수 있습니다.
현수는 이 중 3장을 뽑아 각 카드에 적힌 수를 합한 값을 기록하려 고 합니다.
3장을 뽑을 수 있는 모든 경우를 기록합니다.
기록한 값 중 K번째로 큰 수를 출력 하는 프로그램을 작성하세요.
만약 큰 수부터 만들어진 수가 25 25 23 23 22 20 19......이고
K값이 3이라면 K번째 큰 값 은 22입니다.

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
    n,k = map(int,input().split())
    a = list(map(int,input().split()))

    result = list()
    for i in range (0,n):
        for j in range (0,n):
            if i !=j :
                for h in range (0,n):
                    if i!=h and j!=h:
                        result.append(a[i]+a[j]+a[h])
                        #print(i,j,h)


    result = set(result)
    result = list(result)
    result.sort()
    print(result[-k])
    
    

#################################################################
    print("\n"+output_file.read()+"\n####################\n")

    


