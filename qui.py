numbers=[4,7,9,11,29]
for n in numbers:
    is_prime=True
    for num in range(2,n):
        if(n%num==0):
            is_prime=False
            break
    if(is_prime):
        print(n,'is prime')
    else:
        print(n,'is not prime')
