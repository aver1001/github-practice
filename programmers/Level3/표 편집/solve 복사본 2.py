def solution(n, k, cmd):
    answer = ''

    linked_list = {i: [i - 1, i + 1] for i in range(1, n+1)} #n=8일때 1~8까지
    answer = ["O" for i in range(1,n+1)]
    stack = []

    k += 1

    for cmd in cmd:
        
        if cmd[0] == 'U':
            for _ in range (int(cmd.split(' ')[-1])):
                k = linked_list[k][0]

        elif cmd[0] == 'D':
            for _ in range (int(cmd.split(' ')[-1])):
                k = linked_list[k][1]
            
        elif cmd[0] == 'C':
            pre,next = linked_list[k]
            stack.append([pre,next,k])
            answer[k-1] = 'X'

            if pre == 0:
                linked_list[next][0] = pre
            elif next == n+1:
                linked_list[pre][1] = next
            else:
                linked_list[pre][1] = next
                linked_list[next][0] = pre

            if next == n+1:
                k = pre
            else:
                k = next
            
        elif cmd[0] == 'Z':
            pre,next,temp = stack.pop()
            answer[temp-1] = 'O'

            if pre == 0:
                linked_list[next][0] = temp
            elif next == n+1:
                linked_list[pre][1] = temp
            else:
                linked_list[pre][1] = temp
                linked_list[next][0] = temp

    return ''.join(answer)
            

print(solution(8,2,["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]))






