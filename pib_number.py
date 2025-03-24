a,b=1,0

for i in range(101):
    a,b=b,a+b
    print('{}th Pib. Number is {}'.format(i+2,b))
