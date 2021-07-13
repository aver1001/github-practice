'''
현수의 농장은 N*N 격자판으로 이루어져 있으며,
각 격자안에는 한 그루의 사과나무가 심어저 있다.
N의 크기는 항상 홀수이다.
가을이 되어 사과를 수확해야 하는데 현수는 격자판안의 사 과를 수확할 때
다이아몬드 모양의 격자판만 수확하고 나머지 격자안의 사과는 새들을 위해서 남겨놓는다.
현수과 수확하는 사과의 총 개수를 출력하세요.
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
    ## n//2 +1

    n = int(input())
    a = list()
    for i in range (n):
        a.append(list(map(int,input().split())))

    result = 0
    for i in range (n):
        if i < n//2:
            result += sum(a[i][n//2-i:n//2+1+i])
            result += sum(a[n-i-1][n//2-i:n//2+1+i])
        elif i == n//2:
            result += sum(a[i][:])

        

                

    
#################################################################
    print(result)
#################################################################
    print("\n"+output_file.read()+"\n####################\n")
end = time.time()
print('time elapsed', end - start)

    


