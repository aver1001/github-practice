'''


'''
import sys
import time
def Combination (x,y):

    a=1
    b=1
    for i in range (x,0,-1):
        a *=i
    for i in range (y,0,-1):
        b *=i
    for i in range (x-y,0,-1):
        b *=i

    return a//b

def Combination_List (x):

    result = list()
    for i in range (x+1):
        result.append(Combination (x,i))

    return result

def Cal_Pascal(x,y):
    hap = 0
    for i in range (n):
        hap += x[i]*y[i]

    if hap == f:
        return True
    else :
        return False



def DEF (v,res):

    if v == n:
        #print(res)
        if Cal_Pascal(res,Combination_List(v-1)) :
            print(res)
            end = time.time()
            print('time elapsed', end - start)
            exit()
        return

    
    for i in range (1,n+1):
        try:
            res.index(i)
        except:
            temp = res.copy()
            temp.append(i)
            DEF(v+1,temp)
        



start = time.time()
for sn in range (5,6):
    sn = str(sn)
    input_file_name = 'in' + sn +'.txt'
    output_file_name = 'out' + sn +'.txt'
    
    sys.stdin = open (input_file_name, "rt",encoding = 'utf-8')
    output_file = open(output_file_name, "rt",encoding = 'utf-8')

#################################################################
    n,f = map(int,input().split())
    DEF(0,list())

    
                

    
#################################################################
    print(n,f,sep = ' ')
#################################################################
    print("\n"+output_file.read()+"\n####################\n")
end = time.time()
print('time elapsed', end - start)

    


