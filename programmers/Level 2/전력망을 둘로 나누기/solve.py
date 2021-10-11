from collections import deque
def dfs(start,tree):
    queue = deque([start])
    marked = {start}
    while queue:
        v = queue.popleft()
        for w in tree[v]:
            if w not in marked:
                queue.append(w)
                marked.add(w)
    return len(marked)

def solution(n, wires):
    answer = n
    tree = {k:set() for k in range(1,n+1)}
    for a,b in wires:
        tree[a].add(b)
        tree[b].add(a)
    for a,b in wires:
        tree[a].remove(b)
        tree[b].remove(a)
        result = abs(2*dfs(a,tree)-n)
        tree[a].add(b)
        tree[b].add(a)
        answer = min(answer,result)
    return answer
    


            

solution(7 , [[1, 4], [6, 3], [2, 5], [5, 1], [5, 3],[4,7]]) ##2
#solution(9 , [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]) ## 3
#solution(4 , [[1,2],[2,3],[3,4]]) ## 0
#solution(7 , [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]) ## 1
