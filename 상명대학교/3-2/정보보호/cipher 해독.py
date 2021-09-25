

f = open('cipher.txt',"r",encoding='euc-kr')
alpha = ['E','A','T','O','I','S','R','N','L','D','H','U','C','M','P','F','G','Y','W','B','V','K','X','Q','J','Z']
data = f.read()
print(data)
table = {}
change = {}
for i in range (65,91):
    table[chr(i)] = 0

for i in data:
    if i in table:
        table[i] += 1

temp = list(table.items())
temp.sort(key = lambda x:-x[1])
for (a,b),c in zip(temp,alpha):
    print(a ,'=>',b, '=>',c)
    change[a] = c

print(data)

for i in data:
    if i in change:
        print(change[i],end = '')
    else:
        print(i,end = '')


