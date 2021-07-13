'''

지니레코드에서는 불세출의 가수 조영필의 라이브 동영상을 DVD로 만들어 판매하려 한다.
DVD에는 총 N개의 곡이 들어가는데, DVD에 녹화할 때에는 라이브에서의 순서가 그대로 유지 되어야 한다.
순서가 바뀌는 것을 우리의 가수 조영필씨가 매우 싫어한다.
즉, 1번 노래와 5번 노래를 같은 DVD에 녹화하기 위해서는 1번과 5번 사이의 모든 노래도 같은 DVD에 녹화해야 한다.
또한 한 노래를 쪼개서 두 개의 DVD에 녹화하면 안된다.
지니레코드 입장에서는 이 DVD가 팔릴 것인지 확신할 수 없기 때문에
이 사업에 낭비되는 DVD를 가급적 줄이려고 한다.
고민 끝에 지니레코드는 M개의 DVD에 모든 동영상을 녹화하기 로 하였다.
이 때 DVD의 크기(녹화 가능한 길이)를 최소로 하려고 한다.
그리고 M개의 DVD는 모두 같은 크기여야 제조원가가 적게 들기 때문에 꼭 같은 크기로 해야 한다.
'''
import sys
import time

def count(cap):
    cnt = 1
    sum = 0
    for i in a:
        if sum+i > cap:
            cnt+=1
            sum =i
        else:
            sum+=i

    return cnt
start = time.time()
for sn in range (1,6):
    sn = str(sn)
    input_file_name = 'in' + sn +'.txt'
    output_file_name = 'out' + sn +'.txt'
    
    sys.stdin = open (input_file_name, "rt",encoding = 'utf-8')
    output_file = open(output_file_name, "rt",encoding = 'utf-8')

#################################################################

    # n개의 곡 m개의 dvd
    
    n,m = map(int,input().split())
    a = list(map(int,input().split()))

    lt,rt = 1,sum(a)
    
    maxx= max(a)
    res = 0
    while(lt <= rt):
        #print(lt,rt)
        mid = (lt+rt)//2
        
        if mid >= maxx and count(mid) <= m:
            rt = mid-1
            res = mid
        else:
            lt = mid +1
                

        

    '''
    min_n = 10000
    for i in range (1,n):
        one = sum(a[:i])
        if one >= min_n :
            continue
        else:
            for j in range (i,n-1):
                print(min_n)
                #print(max(sum(a[:i]),sum(a[i:j+1]),sum(a[j+1:])))
                two = sum(a[i:j+1])
                three = sum(a[j+1:])
                res = max(one,two,three)
                if min_n > res:
                    min_n = res
    '''
#################################################################
    print(res)
    #print(n,m,a,sep = '\n')
#################################################################
    print("\n"+output_file.read()+"\n####################\n")
end = time.time()
print('time elapsed', end - start)

    


