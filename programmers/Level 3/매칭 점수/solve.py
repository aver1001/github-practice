def solution(word, pages):
    table = {}
    word = word.upper()
    for first in pages:
        
        head = first.split('<head>\n')[1]
        head = head.split('\n</head>')[0]
        
        body = first.split('<body>\n')[1]
        body = body.split('\n</body>')[0]


        ##head 에서 URL 구하기
        thisurl = head.split('content="')[1]
        thisurl = thisurl[:-3]
        if thisurl not in table:
            table[thisurl] = {'BaseScore':0,'OutUrl':0,'Mechoise':[]}
        

        ##body 에서 외부 URL 구하기
        outurl = []
        temp = body.split('\n<a href="')[1:]
        cnt = 0
        for i in temp:
            cnt += 1
            a = i.split('">')[0]
            outurl.append(a)
            if a not in table:
                table[a] = {'BaseScore':0,'OutUrl':0,'Mechoise':[thisurl]}
            else:
                table[a]['Mechoise'].append(thisurl)
                
        table[thisurl]['OutUrl'] = cnt

        ##body 에서 글 내용 구하기
        print(word)
        print(body)
        
        info = body.split('\n<a href="')[0].upper()
        lt,rt = 0,1
        cnt = 0
        for i in range (len(info)-1):
            if 65 <= ord(info[rt]) <= 90:
                rt += 1
            else:
                if info[lt:rt] == word:
                    cnt += 1
                lt = rt+1
                rt += 1
        print(cnt)
        print()
        table[thisurl]['BaseScore'] = cnt

        ## baseScore 기본점수
        ## len(outurl) 외부 링크 수
        ##
    Max = 0
    for idx,url in enumerate(table):
        print(table[url])
        temp = table[url]['BaseScore'] + sum([table[i]['BaseScore'] / table[i]['OutUrl']for i in table[url]['Mechoise']])
        if temp > Max:
            answer = idx
            Max = temp
    print(answer)

solution('blind',
         ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"])
