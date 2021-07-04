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
    a=input()
    stack=[]
    res=''
    for x in a:
        if x.isdecimal():
            res+=x
        else:
            if x=='(':
                stack.append(x)
            elif x=='*' or x=='/':
                while stack and (stack[-1]=='*' or stack[-1]=='/'):
                    res+=stack.pop()
                stack.append(x)
            elif x=='+' or x=='-':
                while stack and stack[-1]!='(':
                    res+=stack.pop()
                stack.append(x)
            elif x==')':
                while stack and stack[-1]!='(':
                    res+=stack.pop()
                stack.pop()
    while stack:
        res+=stack.pop()

    print(res)
    

    
    
#################################################################
#################################################################
    print("\n"+output_file.read()+"\n####################\n")
end = time.time()
print('time elapsed', end - start)

    


