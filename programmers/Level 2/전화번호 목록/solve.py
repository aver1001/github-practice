def solution(phone_book):
    for i in range (len(phone_book)):
        for j in range (len(phone_book)):
            if i != j:
                print(phone_book[i],phone_book[j][:len(phone_book[i])])
                if phone_book[i] == phone_book[j][:len(phone_book[i])]:
                    return False
        
    return True


phone_book = ["123", "456", "789"]
answer = False

print(solution(phone_book))
