'''
1부터 9까지의 자연수로 채워진 7*7 격자판이 주어지면 격자판 위에서
가로방향 또는 세로방향으로 길이 5자리 회문수가
몇 개 있는지 구하는 프로그램을 작성하세요.
회문수란 121과 같이 앞에서부터 읽으나 뒤에서부터 읽으나 같은 수를 말합니다.

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
    a = list()
    cnt = 0
    for i in range (7):
        a.append(list(map(int,input().split())))

    for i in range (7):
        for j in range(0,3):
            s_list = list()
            #가로
            if (a[i][j:j+5]) == (list(reversed(a[i][j:j+5]))):
                #print("회문 발견!")
                cnt += 1
            #세로
            for k in range (5):
                s_list.append(a[j+k][i])
            if s_list == list(reversed(s_list)):
                #print("회문 발견!")
                cnt += 1

    ##세로 
                
    

    
#################################################################
    print(cnt)
#################################################################
    print("\n"+output_file.read()+"\n####################\n")
end = time.time()
print('time elapsed', end - start)

    


