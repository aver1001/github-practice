'''


'''
import sys
import time
def changeList(num):
    temp = list()

    while(num != 0):
        temp.append(num % 10)
        num = num // 10

    return temp

def changeALP(num):
    if num >= 1 and num <=26:
        return chr(num+64)
    else:
        #print("flow!!")
        return False

def DEF(res,remain):
    print(res,remain)
    global cnt
    
    #print(res,remain)
    if remain:
        if len(remain) == 1:
            one = remain.pop(0)
            if changeALP(one):
                DEF(res+changeALP(one),remain)
            remain.insert(0,one)
        else:
            if remain[1] == 0:
                one = remain.pop(0)
                two = remain.pop(0)
                if changeALP(one*10):
                    DEF(res+changeALP(one*10),remain)
            else:
                one = remain.pop(0)
                DEF(res+changeALP(one),remain)
                two = remain.pop(0)
                temp = one*10 + two
                if changeALP(temp):
                    DEF(res+changeALP(temp),remain)
            remain.insert(0,two)
            remain.insert(0,one)
        
    else:
        print(res)
        cnt +=1
        return
    

start = time.time()
for sn in range (3,4):
    sn = str(sn)
    input_file_name = 'in' + sn +'.txt'
    output_file_name = 'out' + sn +'.txt'
    
    sys.stdin = open (input_file_name, "rt",encoding = 'utf-8')
    output_file = open(output_file_name, "rt",encoding = 'utf-8')

#################################################################
    n = int(input())
    a = changeList(n)
    a.reverse()
    global cnt
    cnt = 0
    DEF('',a)
    print(cnt)

            

    
#################################################################
    #print(n,a,sep='\n')
#################################################################
    #print("\n"+output_file.read()+"\n####################\n")
end = time.time()
print('time elapsed', end - start)
