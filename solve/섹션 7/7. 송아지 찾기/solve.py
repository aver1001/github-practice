'''


'''
import sys
import time
def findCow(s,e):
    distance = e-s
    cnt = 0
    if distance > 0:
        while (distance > 5) :
            cnt += distance // 5
            distance = distance % 5
        if distance == 4:
            cnt +=2
        else:
            cnt += distance

        return cnt

    else:
        return abs(distance)

start = time.time()
for sn in range (1,6):
    sn = str(sn)
    input_file_name = 'in' + sn +'.txt'
    output_file_name = 'out' + sn +'.txt'
    
    sys.stdin = open (input_file_name, "rt",encoding = 'utf-8')
    output_file = open(output_file_name, "rt",encoding = 'utf-8')

#################################################################
    s,e = map(int,(input().split()))

    print(findCow(s,e))
    
                

    
#################################################################
    #print(s,e)
#################################################################
    print("\n"+output_file.read()+"\n####################\n")
end = time.time()
print('time elapsed', end - start)

    


