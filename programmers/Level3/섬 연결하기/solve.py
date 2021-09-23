from collections import deque

n = 4
costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]
##################################################
table = {i : [] for i in range (n)}
check = [0]*n
    
for x,y,cost in costs:
    table[x].append([x,y,cost])
    table[y].append([y,x,cost])
    
for i in range (n):
    table[i].sort(key = lambda x:x[2])
    
costs.sort(key = lambda x:x[2])
answer = 0
queue = [costs[0]]

while (0 in check):
    x,y,cost = queue.pop(0)
    print(check,end = ' ')
    if check[x] == 0 or check[y] == 0:
        print(x,y)
        check[x] = 1
        check[y] = 1
        answer += cost
        queue.extend(table[x])
        queue.extend(table[y])
        queue.sort(key = lambda x:x[2])
        
print(answer)

