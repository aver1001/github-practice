'''

N개의 문자열 데이터를 입력받아
앞에서 읽을 때나 뒤에서 읽을 때나 같은 경우(회문 문자열) 이면 YES를 출력하고
회문 문자열이 아니면 NO를 출력하는 프로그램을 작성한다.
단 회문을 검사할 때 대소문자를 구분하지 않습니다.
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
    ## n은 문자열 갯수
    n = int(input())
    a = list()
    for i in range (n):
        a.append(input())

    cnt = 0
    for i in a:
        cnt +=1
        i = i.lower()
        #print(i, i[::-1])
        if i == i[::-1]:
            print ("#"+str(cnt),'YES')
        else :
            print("#"+str(cnt),'NO')
    
                

    
#################################################################
    
#################################################################
    print("\n"+output_file.read()+"\n####################\n")
end = time.time()
print('time elapsed', end - start)

    


