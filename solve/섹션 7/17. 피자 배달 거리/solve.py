'''


'''
import sys
import time

def findCoor(arr):

    home = list()
    pizza = list()
    for y in range (n):
        for x in range (n):
            if arr[x][y] == 1:
                home.append([x,y])
            elif arr[x][y] == 2:
                pizza.append([x,y])

    return home,pizza


'''
def findDelivery():
    distance = list()
    ## m개 고르기
        


    
    for i in home:
        for j in pizza:
            if (abs(i[0]-j[0]) + abs(i[1]-j[1])) < mins:
                mins = (abs(i[0]-j[0]) + abs(i[1]-j[1]))
        distance.append(mins)
    
    return distance
'''

def DEF(v,res):
    #print(res,v)
    global mins
    
    if len(res) == m :
        sums = 0
        #print(res)
        for i in home:
            distance = list()
            for j in res:
                distance.append(abs(i[0]-j[0]) + abs(i[1]-j[1]))
            #print(distance)
            sums += min(distance)
            if sums > mins:
                break
        if sums < mins:
            print(mins ,"=>",sums)
            mins = sums
                
        return
    for i in range (len(pizza)):
        temp = res.pop(i)
        DEF(v+1,res)
        res.insert(i,temp)

            
start = time.time()
for sn in range (1,6):
    sn = str(sn)
    input_file_name = 'in' + sn +'.txt'
    output_file_name = 'out' + sn +'.txt'
    
    sys.stdin = open (input_file_name, "rt",encoding = 'utf-8')
    output_file = open(output_file_name, "rt",encoding = 'utf-8')

#################################################################
    n,m = map(int,input().split())
    a = list()
    for i in range(n):
        a.append(list(map(int,input().split())))
    global mins
    mins = 9999

    home, pizza = findCoor(a)
    #print(m)
    #print("Home",len(home),"Pizza",len(pizza))
    DEF(1,pizza)

    print(mins)


    

    

    
#################################################################
    #print(a)
#################################################################
    print("\n"+output_file.read()+"\n####################\n")
end = time.time()
print('time elapsed', end - start)

    


