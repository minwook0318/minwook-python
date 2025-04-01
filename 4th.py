for i in range(1, 10):
    print(f"2 * {i} = {2 * i}")
    
i = 1
while i <= 9:
    print(f"2 * {i} = {2 * i}")
    i += 1

for i in range(3):
     print('Python')
     print('is')
     print('FUN! ')

for i in range(3):
     print('Python')
     print('is')
print('FUN! ')

for i in range(3):
     print('Python ')
print('is ')
print('FUN! ')
#4.5
menu = {'b': '햄버거',  'c': '치킨',  'p': '피자'}
while True:
    choice = input("메뉴를 선택하세요(알파벳 b, c, p 입력): ").lower()
    if choice in menu:
        print(f"{menu[choice]}을 선택하였습니다.")
        break
    else:
        print("메뉴를 다시 입력하세요.")
#4.7
n = int(input("숫자를 입력하세요: "))
is_prime = True

if n <= 1:
    is_prime = False
elif n == 2:
    is_prime = True
elif n % 2 == 0:
    is_prime = False
else:
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            is_prime = False
            

print(f"{n}는 소수{'입니다' if is_prime else '가 아닙니다'}.")

#4.9
n = int(input("숫자를 입력하세요: "))
result = sum(i**2 for i in range(1, n+1))
print(f"결과는 {result}입니다.")

#4.11
depth = 30
position = 0
days = 0

while position < depth:
    days += 1
    position += 7
    if position >= depth:
        break
    position -= 5
    print(f"day: {days}    달팽이의 위치: {position} 미터")

print(f"우물을 탈출하는 데 걸린 날은 {days}일입니다.")

#4.13
for num in range(100, 1000):
    sum_cubes = sum(int(digit)**3 for digit in str(num))
    if sum_cubes == num:
        print(num, end=" ")
        
#4.15
fuel = 500

while True:
    action = input("충전 또는 사용한 연료를 +/- 기호와 함께 입력하시오: ")
    fuel += int(action)
    print(f"현재 탱크양은 {fuel} 입니다.")
    
    if fuel < 50:  # 10% of 500
        print("경고: 연료가 10% 미만이니 충전하세요!")
        break
