'''

N개의 자연수가 입력되면 각 자연수를 뒤집은 후
그 뒤집은 수가 소수이면 그 수를 출력하는 프로그램을 작성하세요.
예를 들어 32를 뒤집으면 23이고, 23은 소수이다. 그러면 23을 출력 한다.
단 910를 뒤집으면 19로 숫자화 해야 한다. 첫 자리부터의 연속된 0은 무시한다.
뒤집는 함수인 def reverse(x) 와 소수인지를 확인하는 함수 def isPrime(x)를
반드시 작성하 여 프로그래밍 한다.

'''
import sys
import time

def reverse(x):
    result = list()
    for i in range(n):
        temp = 0
        b=list(map(int,reversed(str(x[i]))))
        for j in range (1,len(b)+1):
            temp += (b[-j]*(10**(j-1)))
        result.append(temp)

    return result

def isPrime(x):
    result = list(x)
    for i in range (n):
        if x[i] == 1:
            result.remove(x[i])
        for j in range (2,x[i]):
            if (x[i]%j == 0):
                result.remove(x[i])
                break

    return result



start = time.time()
for sn in range (1,6):
    sn = str(sn)
    input_file_name = 'in' + sn +'.txt'
    output_file_name = 'out' + sn +'.txt'
    
    sys.stdin = open (input_file_name, "rt",encoding = 'utf-8')
    output_file = open(output_file_name, "rt",encoding = 'utf-8')
    print("############["+sn+"]############\n")
#################################################################
    
    n = int(input())
    a = list(map(int,input().split()))


    result = reverse(a)
    result = isPrime(result)
    
    

#################################################################
    print(result)
   
#################################################################
    print("\n"+output_file.read()+"\n")
end = time.time()
print('time elapsed', end - start)

    


