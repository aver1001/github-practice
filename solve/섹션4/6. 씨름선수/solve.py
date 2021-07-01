'''
현수는 씨름 감독입니다.
현수는 씨름 선수를 선발공고를 냈고, N명의 지원자가 지원을 했습 니다.
현수는 각 지원자의 키와 몸무게 정보를 알고 있습니다.
현수는 씨름 선수 선발 원칙을 다음과 같이 정했습니다.
“다른 모든 지원자와 일대일 비교하여
키와 몸무게 중 적어도 하나는 크거나,무거운 지원자 만 뽑기로 했습니다.”
만약 A라는 지원자보다 키도 크고 몸무게도 무거운 지원자가 존재한다면
A지원자는 탈락입니 다.

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
    n = int(input())
    a = list()
    
    for i in range (n):
        a.append(list(map(int,input().split())))

    cnt = 0
    
    for i in range (n):
        temp = 0
        for j in range(n):
            if j != i:
                #print(i,j)
                if a[i][0] > a[j][0] or a[i][1] > a[j][1] : ##
                    temp +=1
                else :
                    break
        if temp == n-1:
            cnt +=1

                
                

    
#################################################################
    print(cnt)
#################################################################
    print("\n"+output_file.read()+"\n####################\n")
end = time.time()
print('time elapsed', end - start)

    


