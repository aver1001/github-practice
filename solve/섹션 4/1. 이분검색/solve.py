'''
임의의 N개의 숫자가 입력으로 주어집니다.
N개의 수를 오름차순으로 정렬한 다음
N개의 수 중 한 개의 수인 M이 주어지면 이분검색으로
M이 정렬된 상태에서 몇 번째에 있는지 구하는 프로그램을 작성하세요.
단 중복값은 존재하지 않습니다.

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
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()

    
#################################################################
    print(a.index(m)+1)
#################################################################
    print("\n"+output_file.read()+"\n####################\n")
end = time.time()
print('time elapsed', end - start)

    


