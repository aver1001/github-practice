'''
N개의 수로 된 수열 A[1], A[2], ..., A[N] 이 있다.
이 수열의 i번째 수부터 j번째 수까지의 합 A[i]+A[i+1]+...+A[j-1]+A[j]가
M이 되는 경우의 수를 구하는 프로그램을 작성하시오.


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


    
    ## 입력
    ## n 수열의 개수 m합
    ## 수열

    n, m = map(int,input().split())
    a = list(map(int,input().split()))

    '''
    시간복잡도 너무 높음 탈락.
    
    cnt = 0
    for i in range (n):
        # 1~n 개 선택
        if i>m : break
        for j in range (n-i):
            if m == sum(a[j:j+i+1]) :
                cnt +=1
    '''
    cnt = 0
    #print(a)
    #print(n,m)
    lt,rt = 0,1
    tot=a[0]
    cnt=0
    while True:
        if tot<m:
            if rt<n:
                tot+=a[rt]
                rt+=1
            else:
                break
        elif tot==m:
            cnt+=1
            tot-=a[lt]
            lt+=1
        else:
            tot-=a[lt]
            lt+=1
    print(cnt)
    
#################################################################
    print("\n"+output_file.read()+"\n####################\n")
end = time.time()
print('time elapsed', end - start)

    


