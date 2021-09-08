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
    
    cycle = lcmarr(times)
    cycle_count = cycleCount(times,cycle)
    count = cycle_count
    count_time = cycle
    while (count <= n):
        count += cycle_count
        count_time += cycle
    
    while (count != n):
        
        count_time -= times[-1] - times[-2]
        count -= 1
        times.insert(0,times[-1] - times[-2])
        times.pop()
        print(count,count_time, times)
    print(count_time)
    

solution(6,[7,10])        
        
