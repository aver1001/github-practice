'''


'''
import sys
import time
def DEF (v,person):
    global mins
    
    if v == n:
        try:
            temp = max(person) - min(person)
            if temp < mins and person[0] != person [1] and person[1] != person[2] and person[0] != person [2]:
                mins = temp
            return
        except:
            return
        

    for i in range(3):
        person[i] += a[v]
        DEF(v+1,person)
        person[i] -= a[v]

start = time.time()
for sn in range (1,6):
    sn = str(sn)
    input_file_name = 'in' + sn +'.txt'
    output_file_name = 'out' + sn +'.txt'
    
    sys.stdin = open (input_file_name, "rt",encoding = 'utf-8')
    output_file = open(output_file_name, "rt",encoding = 'utf-8')

#################################################################
    n = int(input())
    a = list()
    global mins
    mins = 99999
    for i in range(n):
        a.append(int(input()))
    person = [0]*3

    DEF(0,person)
    print(mins)

    
#################################################################
    #print(n,a,person,sep='\n')
#################################################################
    print("\n"+output_file.read()+"\n####################\n")
end = time.time()
print('time elapsed', end - start)

    


