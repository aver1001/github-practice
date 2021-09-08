def solution(arr):
    for i in arr : print(i)
    print()
    cntone = 0
    cntzero = 0
    check = 0
    for i in arr:
        for j in i:
            if arr[0][0] != j:
                check = 1
    if check == 0:
        if arr[0][0] == 1:
            return [0,1]
        else:
            return [1,0]
    arrqueue = [arr]


    
    while (arrqueue):
        q = arrqueue.pop(0)
        print(q)
        if q == 1:
            cntone += 1
            continue
        elif q == 0:
            cntzero += 1
            continue
        
        n = len(q)
        print(n)
        print(cntzero,cntone)
        for a,b in [[0,n//2],[n//2,n]]:

            tempArr = []
            check = 0
            checkNum = q[0][a]
            print(checkNum,0,a)
            for i in range (0,n//2):
                if any(j != checkNum for j in q[i][a:b]):
                    check = 1
                tempArr.append(q[i][a:b])

            print(tempArr)
            if check == 1:
                print('diffrent')
                arrqueue.append(tempArr)
            else:
                print('same')
                arrqueue.append(checkNum)
                
            print()
            tempArr = []
            check = 0
            checkNum = q[n//2][a]
            print(checkNum,n//2,[a])
            for i in range (n//2,n):
                if any(j != checkNum for j in q[i][a:b]):
                    check = 1
                tempArr.append(q[i][a:b])
            print(tempArr)
            if check == 1:
                print('diffrent')
                arrqueue.append(tempArr)
            else:
                print('same')
                arrqueue.append(checkNum)
                
            print()
        

            
    return [cntzero,cntone]

    


a = solution([[0,0],[0,0]])
print(a)
