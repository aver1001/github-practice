'''

N개의 자연수가 입력되면 각 자연수의 자릿수의 합을 구하고,
그 합이 최대인 자연수를 출력 하는 프로그램을 작성하세요.
각 자연수의 자릿수의 합을 구하는 함수를 def digit_sum(x)를
꼭 작성해서 프로그래밍 하세요.

'''
def digit_sum(x):
    result = list()
    while (x > 0):
        result.append(x % 10)
        x = x // 10

    return sum(result)


import sys


for sn in range (1,6):
    sn = str(sn)
    input_file_name = 'in' + sn +'.txt'
    output_file_name = 'out' + sn +'.txt'
    
    sys.stdin = open (input_file_name, "rt")
    output_file = open(output_file_name, "rt")

#################################################################
    n = int(input())
    digit=list(map(int,input().split()))

    result = list()
    for i in range (n):
        result.append(digit_sum(digit[i]))

    #print(digit)
    #print(result)
    print(digit[result.index(max(result))])
#################################################################
    print("\n"+output_file.read()+"\n####################\n")

    


