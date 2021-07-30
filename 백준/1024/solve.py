'''


'''
import sys
import time

def findCodon (dna):
    global result
    dna = str.join('',dna)
    temp = ''
    for i in range (0,len(dna),3):
        if dna[i:i+3] in codon:
            temp += codon[dna[i:i+3]]
    result.add(temp)
    

def DFE(v,dna):
    if v == Maximum:
        return
    findCodon(dna)

    for i in range (len(dna)):
        temp = dna.pop(i)
        DFE(v+1,dna)
        dna.insert(i,temp)

    
    

start = time.time()
for sn in range (1,2):
    sn = str(sn)
    input_file_name = 'in' + sn +'.txt'
    output_file_name = 'out' + sn +'.txt'
    
    sys.stdin = open (input_file_name, "rt",encoding = 'utf-8')
    output_file = open(output_file_name, "rt",encoding = 'utf-8')

#################################################################
    dna = list(input())
    Maximum =len(dna) - 2
    tnum = int(input())
    codon = dict()
    global result
    result = set()
    for i in range(tnum):
        a,b = input().split(' ')
        codon[a] = b
    DFE(0,dna)

    print(len(result))

    
    

    
    

    

#################################################################
    print("\n"+output_file.read()+"\n####################\n")
end = time.time()
print('time elapsed', end - start)

    


