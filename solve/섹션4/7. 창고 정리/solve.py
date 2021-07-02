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
    L = int(input())
    box = list(map(int,input().split()))
    M = int(input())
    for i in range (M):
        box[box.index(max(box))] -=1
        box[box.index(min(box))] +=1
    
                    

    
#################################################################
    print(max(box)-min(box),sep = '\n')
#################################################################
    print("\n"+output_file.read()+"\n####################\n")
end = time.time()
print('time elapsed', end - start)

    


