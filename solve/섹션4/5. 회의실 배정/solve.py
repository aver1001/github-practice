'''
한 개의 회의실이 있는데 이를 사용하고자 하는 n개의 회의들에 대하여 회의실 사용표를 만들 려고 한다.
각 회의에 대해 시작시간과 끝나는 시간이 주어져 있고,
각 회의가 겹치지 않게 하 면서 회의실을 사용할 수 있는 최대수의 회의를 찾아라.
단, 회의는 한번 시작하면 중간에 중 단될 수 없으며
한 회의가 끝나는 것과 동시에 다음 회의가 시작될 수 있다.

'''
import sys
import time


start = time.time()
for sn in range (1,2):
    sn = str(sn)
    input_file_name = 'in' + sn +'.txt'
    output_file_name = 'out' + sn +'.txt'
    
    sys.stdin = open (input_file_name, "rt",encoding = 'utf-8')
    output_file = open(output_file_name, "rt",encoding = 'utf-8')

#################################################################
    n = int(input())
    times = []
    for i in range (n):
        a,b = map(int,input().split())
        times.append((a,b))
    times.sort(key = lambda x : (x[1],x[0]))
    #print(times)

    et = 0
    cnt = 0

    for x,y in times:
        print(et, y)
        if et <= x:
            print("!!")
            et = y
            cnt +=1
            
    print(cnt)
    


    '''
    times = [0 for _ in range(24)]
    #print(times)

    cnt = 0
    for j in range (1,25):
        print(j)
        for i in range(n):
            print(a[i][:],a[i][1]-a[i][0])
            if a[i][1]-a[i][0] == j:
                for k in range (j):
                    times[a[i][1]-3+k] = 1
                print(times)
                cnt +=1
            #print(a[i][:],a[i][1]-a[i][0])
    '''
                

    
#################################################################
    #print(n,a,sep = '\n')
#################################################################
    print("\n"+output_file.read()+"\n####################\n")
end = time.time()
print('time elapsed', end - start)

    


