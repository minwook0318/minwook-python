a,b=0,1
for i in range(101):
    print('{}th Pib. Number is {}'.format(i,a))
    b=a+b
    a=b-a
