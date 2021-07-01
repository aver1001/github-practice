'''
N개의 마구간이 수직선상에 있습니다.
각 마구간은 x1, x2, x3, ......, xN의 좌표를 가지며, 마 구간간에 좌표가 중복되는 일은 없습니다.
현수는 C마리의 말을 가지고 있는데, 이 말들은 서로 가까이 있는 것을 좋아하지 않습니다.
각 마구간에는 한 마리의 말만 넣을 수 있고, 가장 가까운 두 말의 거리가 최대가 되게 말을 마구간에 배치하고 싶습니다.
C마리의 말을 N개의 마구간에 배치했을 때 가장 가까운 두 말의 거리가 최대가 되는 그 최대 값을 출력하는 프로그램을 작성하세요.

'''
import sys
import time

def judge (distance):

    before = a[0]
    cnt = 1
    for i in a:
        if i - before >= distance:
            cnt +=1
            before = i
            
    return cnt
            
        
start = time.time()
for sn in range (1,6):
    sn = str(sn)
    input_file_name = 'in' + sn +'.txt'
    output_file_name = 'out' + sn +'.txt'
    
    sys.stdin = open (input_file_name, "rt",encoding = 'utf-8')
    output_file = open(output_file_name, "rt",encoding = 'utf-8')

#################################################################
    n,c = map(int,input().split())
    a = list()
    for i in range (n):
        a.append(int(input()))
    a.sort()

    lt, rt = 1, max(a)
    while(lt <= rt):
        mid = (lt + rt)//2
        #print(lt,rt, mid, judge(mid))
        if judge(mid) >= c:
            res = mid
            lt = mid +1
        else :
            rt = mid -1
    print(res)
    
#################################################################
    #print(n,c,sep = '\n')
#################################################################
    print("\n"+output_file.read()+"\n####################\n")
end = time.time()
print('time elapsed', end - start)

    


