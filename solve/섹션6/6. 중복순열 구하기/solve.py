'''


'''
import sys
import time
def Card (v,st):
    global cnt
    if v == 0:
        for i in st:
            print(i,end = ' ')
        print()
        cnt +=1
        return
    else:
        for i in range (m):
            Card (v-1,st+str(i+1))
            
start = time.time()
for sn in range (1,6):
    sn = str(sn)
    input_file_name = 'in' + sn +'.txt'
    output_file_name = 'out' + sn +'.txt'
    
    sys.stdin = open (input_file_name, "rt",encoding = 'utf-8')
    output_file = open(output_file_name, "rt",encoding = 'utf-8')

#################################################################
    m,n = map(int,input().split())
    card = list()
    global cnt
    cnt = 0
    for i in range (1,m+1):
        card.append(i)
    Card(n,'')
    print(cnt)
        
                

    
#################################################################
    #print(m,n)
#################################################################
    print("\n"+output_file.read()+"\n####################\n")
end = time.time()
print('time elapsed', end - start)

    


