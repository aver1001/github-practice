'''


'''
import sys
import time
def changeList(num):
    temp = list()

    while(num != 0):
        temp.append(num % 10)
        num = num // 10

    temp.reverse()
    temp.append(-1)

    return temp


def changeALP(num):
    if num >= 1 and num <=26:
        return chr(num+64)
    else:
        print(num)
        #print("flow!!")
        return False
    
def DEF(v,res) :
    global cnt
    #print(v,res)
    if a[v] == 0:
        return
    if v > b:
        #print(res,"over")
        return
    elif v == b-1:
        print(res)
        cnt += 1
        return
    
    ##근본적으로 일의자리냐 십의자리냐

    ##일의자리 숫자일 경우
    
    if a[v+1] != 0:
        #print("+1",res)
        DEF(v+1,res+changeALP(a[v]))

    ##십의자리 숫자일 경우

    if a[v]*10 +a[v+1] >= 10 and  a[v]*10 +a[v+1] <= 26 and a[v+1] != -1:
        if a[v+1] == -1:
            return
        #print("+2",res)
        DEF(v+2,res+changeALP(a[v]*10+a[v+1]))

            
    

start = time.time()
for sn in range (5,6):
    sn = str(sn)
    input_file_name = 'in' + sn +'.txt'
    output_file_name = 'out' + sn +'.txt'
    
    sys.stdin = open (input_file_name, "rt",encoding = 'utf-8')
    output_file = open(output_file_name, "rt",encoding = 'utf-8')

#################################################################
    n = int(input())
    a = changeList(n)
    b = len(a)
    global cnt
    cnt =0
    DEF(0,'')

            


#################################################################
    #print(n,a,sep='\n')
#################################################################
    print("\n"+output_file.read()+"\n####################\n")
    print(cnt)
end = time.time()
print('time elapsed', end - start)
