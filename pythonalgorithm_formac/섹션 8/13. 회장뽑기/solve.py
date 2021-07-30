'''


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
    n = int(input())
    a = [[0] * n for _ in range (n)]
    while(1):
        x,y = map(int,(input().split()))
        if x == -1:
            break
        a[x-1][y-1] = 1
        a[y-1][x-1] = 1

    #for i in a : print(i)
    for i in range (n):
        for j in range (n):
            temp = list()
            if i == j or a[i][j] != 0:
                continue
            for k in range (n):
                #print(i+1,k+1,j+1,a[i][k]+a[k][j])
                if a[i][k] !=0 and a[k][j] != 0:
                    temp.append(a[i][k]+a[k][j])
            a[i][j] = min(temp)
            a[j][i] = min(temp)
            #for q in a: print(q)
            #print()

    person = list()
    for i in a:
        person.append(max(i))

    print(min(person),i.count(min(person)))
    for i in range(n):
        if person[i] == min(person):
            print(i+1,end = ' ')
                

    
#################################################################
    #print(n)
#################################################################
    print("\n"+output_file.read()+"\n####################\n")
end = time.time()
print('time elapsed', end - start)

    


