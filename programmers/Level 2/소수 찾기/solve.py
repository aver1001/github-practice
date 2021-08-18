def DFS (v,f,res,number):
    global numberList
    if v == f:
        numberList.add(int(res))
    else:
        for i in range (len(number)):
            temp = number.pop(i)
            DFS(v+1,f,res+temp,number)
            number.insert(i,temp)
        

def solution(numbers):
    global numberList
    numberList = set()
    numbers = list(numbers)
    numbers.reverse()
    
    n = int(str.join('',numbers))+1
    ## 소수 판별
    a = [False,False] + [True]*(n-1)
    primes=[]
    for i in range(2,n+1):
      if a[i]:
        primes.append(i)
        for j in range(2*i, n+1, i):
            a[j] = False

    print(primes)
    ## 가능한 자연수 계산 
    for i in range (1,len(numbers)+1):
        DFS(0,i,'',numbers)
    numberList = list(numberList)
    
    cnt = 0
    for i in numberList:
        if i in primes:
            cnt +=1

    return cnt

numbers = "011"
print(solution(numbers))
