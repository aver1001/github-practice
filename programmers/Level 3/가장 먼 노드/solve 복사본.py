from collections import deque
def solution(n, edge):
    answer = 0
    graph = [[]* n for _ in range(n+1)] # 각 노트와 연결된 노드표시
    print(graph)
    for a,b in edge:
        graph[a].append(b)
        graph[b].append(a)
    print(graph)
    visited = [0]*(n+1)
    visited[1] = 1
    print(visited)
    queue = deque([1])
    while(queue):
        n = queue.popleft()
       
        for i in graph[n]:
            if visited[i]==0:
                queue.append(i)
                visited[i] = visited[n]+1
        print(queue)
        print(visited)
    answer = visited.count(max(visited))
    return answer

solution(6,[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]])
