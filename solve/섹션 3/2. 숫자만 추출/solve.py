'''

문자와 숫자가 섞여있는 문자열이 주어지면 그 중 숫자만 추출하여 그 순서대로 자연수를 만 듭니다.
만들어진 자연수와 그 자연수의 약수 개수를 출력합니다.
만약 “t0e0a1c2h0er”에서 숫자만 추출하면 0, 0, 1, 2, 0이고 이것을 자연수를 만들면 120이 됩니다.
즉첫자리0은자연수화할때무시합니다.
출력은120를출력하고,다음줄에120 의 약수의 개수를 출력하면 됩니다.
추출하여 만들어지는 자연수는 100,000,000을 넘지 않습니다.

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
    ## 입력 => 숫자가 섞인 문자열
    str1 = input()
    str1 = list(str1)


    
    result = list()
    for i in range (len(str1)):
        if str1[i].isdigit() == True:
            result.append(str1[i])

    #print(result)
    digit = 0
    for i in range (0,len(result)):
        #print(int(result[i])*10**(len(result)-i-1))
        digit += (int(result[i])*10**(len(result)-i-1))

    yak = 0
    for i in range (1,digit+1):
        if (digit % i == 0):
            #print(i)
            yak +=1

    
    
                

    
#################################################################
    print(digit,yak, sep ='\n')
#################################################################
    print("\n"+output_file.read()+"\n####################\n")
end = time.time()
print('time elapsed', end - start)

    


