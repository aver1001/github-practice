def solution(arr):
    arr.sort()
    Max = arr[-1]
    lens = len(arr)-1
    while(True):
        check = 0
        for i in range(lens):
            if (Max /arr[i]) % 1 == 0:
                check += 1
        if lens == check:
            return Max
        Max += arr[-1]


print(solution([1]))
