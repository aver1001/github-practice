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
    a = list(input())

    stack = list()

    while(a):
        temp = a.pop(0)
        
        if temp.isdecimal() == True:
            stack.append(int(temp))
        else:
            if temp == '+':
                stack.append(stack.pop()+stack.pop())
            elif temp == '-':
                stack.append(-stack.pop()+stack.pop())
            elif temp == '*':
                stack.append(stack.pop()*stack.pop())
            elif temp == '/':
                stack.append(stack.pop()/stack.pop())
        #print(stack)
    

    
#################################################################
    print(stack[0])
#################################################################
    print("\n"+output_file.read()+"\n####################\n")
end = time.time()
print('time elapsed', end - start)

    


