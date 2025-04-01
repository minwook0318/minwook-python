primes=[]
for n in range(2,101):
    is_prime=True
    for num in range(2,n):
        if n%num==0:
            is_prime=False
    if is_prime:
        primes.append(n)
print(primes)
