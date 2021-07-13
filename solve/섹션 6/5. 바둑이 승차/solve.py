'''


'''
import sys
import time



def DFS (x,sum_doggy):
    #print(x)
    global result
    if sum_doggy > c:
        return
    if sum > result:
        result = sum
    
    if x == n:
        if sum_doggy < c:
            result.append(sum_doggy)
    
    else:
        DFS(x+1,sum_doggy+doggy[x])
        DFS(x+1,sum_doggy)
        


start = time.time()
for sn in range (1,6):
    sn = str(sn)
    input_file_name = 'in' + sn +'.txt'
    output_file_name = 'out' + sn +'.txt'
    
    sys.stdin = open (input_file_name, "rt",encoding = 'utf-8')
    output_file = open(output_file_name, "rt",encoding = 'utf-8')

#################################################################
    c,n = map(int,input().split())

    result = list()
    result = 0
    doggy = list()
    for i in range (n):
        doggy.append(int(input()))
    DFS(0,0)
    result.sort()
    print(result[-1])

    
#################################################################
    #print(c,n,doggy)
#################################################################
    print("\n"+output_file.read()+"\n####################\n")
end = time.time()
print('time elapsed', end - start)

    


