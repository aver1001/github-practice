alpha = ['E','A','T','O','I','S','R','N','L','D','H','U','C','M','P','F','G','Y','W','B','V','K','X','Q','J','Z']
f = open('plain.txt',"r")
data = f.read()
data = data.upper()
change = {}
table = {}

for i in range (65,91):
    change[chr(i)] = alpha[i-65]
    table[chr(i)] = 0
a = 0
## 암호화
for idx,i in enumerate(data):
    if i in change:
        ## 암호화
        data[idx] = change[i]
        ## 빈도수 체크
        table[data[i]] += 1


for i in table:
    print(i ,'=>',table[i])


'''
