## 에라스토테네스의 체


N = 1000
prime = [True]*N
prime[0],prime[1] = False, False

for i in range(2,N):
    if prime[i] == True:
        for j in range(2*i,N,i):
            prime[j] = False

