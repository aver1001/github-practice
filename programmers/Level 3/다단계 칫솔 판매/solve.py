def solution(enroll, referral, seller, amount):
    table = {}
    result = {}
    
    for enrolls,referrals in zip(enroll,referral):
        table[enrolls] = referrals
        result[enrolls] = 0
        
    for enroll,referral in zip(enroll,referral):
        if referral != '-' :
            table[enroll] = {referral : table[referral]}
            
    print(table)
    for sell,amoun in zip(seller,amount):
        amoun *= 100
        print(sell,amoun)
        while(True):
            if table[sell] == '-':
                if amoun < 10:
                    result[sell] = result[sell] + amoun
                    break
                result[sell] = result[sell] + (amoun - (amoun // 10))
                break
            else:
                if amoun < 10:
                    result[sell] = result[sell] + amoun
                    break
                else:
                    result[sell] = result[sell] + (amoun - (amoun // 10))
                    sell = list(table[sell].keys())[0]
                    amoun = (amoun // 10)
    print(list(result.values()))



solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
         ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
         ["young", "john", "tod", "emily", "mary"],
         [12, 4, 2, 5, 10])
