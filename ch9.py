#9.1
try :
 a, b = input('두 수를 입력하시오 : ').split()
 result = int(a) * int(b)
 print("결과:", result)
except ValueError:
    print("올바른 두 개의 숫자를 입력하세요.")


    a_list = [200, 300, 400]
print('a_list :', a_list)
#
try:
    idx = int(input('구하고자 하는 값의 인덱스를 0,1,2 중에서 입력하시오 : '))
    result = a_list[idx]
except ValueError:
    print("Error: 정수만 입력 가능합니다.")
except IndexError:
    print("Error: 인덱스는 0, 1, 2 중 하나여야 합니다.")
else:
    print('결과 : ', result)
#9.5

with open("number1to10.txt", "w") as file:
    for i in range(1, 11):
        file.write(str(i) + "\n")    
    

#9.9

    with open("coord.txt", "r") as file:
    n = int(file.readline()) 
    coords = []

    for _ in range(n):
        x, y = map(int, file.readline().split())
        coords.append((x, y))


coords.sort()

for x, y in coords:
    print(x, y)
