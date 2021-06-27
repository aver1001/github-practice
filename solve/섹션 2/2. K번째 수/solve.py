'''

N개의 숫자로 이루어진 숫자열이 주어지면 해당 숫자열중에서
s번째부터 e번째 까지의 수를 오름 차순 정렬했을 때
k번째로 나타나는 숫자를 출력하는 프로그램을 작성하세요.
'''
import sys


for sn in range (1,6):
    sn = str(sn)
    input_file_name = 'in' + sn +'.txt'
    output_file_name = 'out' + sn +'.txt'
    
    sys.stdin = open (input_file_name, "rt")
    output_file = open(output_file_name, "rt")

#################################################################

    T = int(input())
    for i in range (0,T):
        n,s,e,k = map(int,input().split())
        a = list(map(int,input().split()))
        #print (n,s,e,k)
        #print (a)
        a = a[s-1:e+2]
        #print (a)
        a.sort()

        #print (a)
        print("#"+str(i+1),a[k-1])
#################################################################
    print("\n"+output_file.read()+"\n####################\n")

    


