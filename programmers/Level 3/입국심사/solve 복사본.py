def gcd(x, y):
    if y: return gcd(y, x%y)
    else: return x

def lcm(x, y):
    return int(x * y / gcd(x, y))

def lcmarr(arr):
    temp = lcm(arr[0],arr[1])
    for i in range (2,len(arr)):
        temp = lcm(temp,arr[i])
    return temp

def cycleCount(arr,t):
    temp = 0
    for i in arr:
        temp += t//i
    return temp

def solution(n, times):
    a = cycleCount(times,lcmarr(times))
    print(a)
    b = n // a
    n = n% len(times)
    res = (times[0]*n+1)
    table = [0]*res
    for i in times:
        for j in range (i,res,i):
            table[j] = table[j]+1
    answer = 0
    for i in range(res):
        answer += table[i]
        if answer >= n:
            break
    return(i+ b)
        
    

print(solution(6,[7,10]))
        
