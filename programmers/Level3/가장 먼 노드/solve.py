from collections import deque
def solution(n, edge):
    table = [[]* n for _ in range(n+1)]
    for x,y in edge:
        table[x].append(y)
        table[y].append(x)
    visited = [0 for _ in range (n+1)]
    visited[1] = 1
    queue = deque([1])
    while(queue):
        a = queue.popleft()
        for i in table[a]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = visited[a]+1
    return visited.count(max(visited))


        


a = solution(6,[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]])
print(a)
