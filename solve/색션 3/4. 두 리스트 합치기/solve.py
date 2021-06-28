'''
오름차순으로 정렬이 된 두 리스트가 주어지면
두 리스트를 오름차순으로 합쳐 출력하는 프로그램을 작성하세요.

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
    ## 입력 1.리스트의 크기 2. 리스트 2번반복
    n = int(input())
    a = list(map(int,input().split()))

    n = int(input())
    b = list(map(int,input().split()))
            
    c = a+b
    c.sort()

    
#################################################################
    for i in c:     
        print(i,end = ' ')
#################################################################
    print("\n"+output_file.read()+"\n####################\n")
end = time.time()
print('time elapsed', end - start)

    


