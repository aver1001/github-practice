'''

OX 문제는 맞거나 틀린 두 경우의 답을 가지는 문제를 말한다.
여러 개의 OX 문제로 만들어진 시험에서 연속적으로 답을 맞히는 경우에는
가산점을 주기 위해서 다음과 같이 점수 계산을 하기 로 하였다. 1번 문제가 맞는 경우에는 1점으로 계산한다.
앞의 문제에 대해서는 답을 틀리다가 답이 맞는 처음 문제는 1점으로 계산한다.
또한, 연속으로 문제의 답이 맞는 경우에서 두 번째 문제는 2점, 세 번째 문제는 3점, ...,
K번째 문제는 K점으로 계산한다.틀린 문제는 0점으로 계 산한다.

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
    ## n은 문제  
    n = int(input())
    a = list(map(int,input().split()))

    cnt = 0
    score = 0
    for i in a:
        if i == 1:
            cnt +=1
        if i == 0:
            cnt = 0
        score += cnt
    
                

    
#################################################################
    print(score)
#################################################################
    print("\n"+output_file.read()+"\n####################\n")
end = time.time()
print('time elapsed', end - start)

    


