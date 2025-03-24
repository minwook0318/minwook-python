n=int(input('수를 입력하세요:'))
is_prime=True
for num in range(2,n):
    if n%num==0:
        is_prime=False
        
print(n,'is_prime:',is_prime)
