
#5.1
def greet():
    print("환영합니다.")

greet()
greet()
#5.5
def inch2cm(inch):
    return inch * 2.54

for i in range(1, 6):
    print(f"{i} 인치 = {inch2cm(i)} 센티미터")
#5.9
def mean_of_n(nums):
    return sum(nums) / len(nums)

def max_of_n(nums):
    return max(nums)

def min_of_n(nums):
    return min(nums)

input_str = input("정수를 여러 개 입력하시오 : ")
nums = list(map(int, input_str.split()))
print(f"평균값은 {mean_of_n(nums)}")
print(f"최댓값은 {max_of_n(nums)}")
print(f"최솟값은 {min_of_n(nums)}")

#5.13
import math

def cube_volume(s):
    return s ** 3
def cuboid_volume(l, w, h):
    return l * w * h
def cone_volume(r, h):
    return (1/3) * math.pi * (r ** 2) * h
def sphere_volume(r):
    return (4/3) * math.pi * (r ** 3)
def cylinder_volume(r, h):
    return math.pi * (r ** 2) * h
print("모서리의 길이가 12인 정육면체의 부피:", cube_volume(12))
print("모서리의 길이가 20인 정육면체의 부피:", cube_volume(20))
print("가로 3, 세로 5, 깊이 6인 직육면체의 부피:", cuboid_volume(3, 5, 6))
print("반지름 20, 높이 10인 원뿔의 부피:", cone_volume(20, 10))
print("반지름 15인 구의 부피:", sphere_volume(15))
print("반지름 20, 높이 10인 원기둥의 부피:", cylinder_volume(20, 10))
#5.17
def sum_range(n1, n2):
    return sum(range(n1, n2 + 1))
print(f"10에서 20까지의 정수의 합: {sum_range(10, 20)}")
print(f"40에서 100까지의 정수의 합: {sum_range(40, 100)}")

#5.21
def format_birthdate(birth):
    year = birth[:2]
    month = birth[2:4]
    day = birth[4:6]
    
    if int(year) <= 49:
        year = "20" + year
    else:
        year = "19" + year
    
    return f"{year}년 {month}월 {day}일"
birth = input("주민등록번호 첫 6숫자 형식 입력: ")
print(format_birthdate(birth))

#5.25
s1 = 'Kang Young Min'
s2 = ' Kang Young-Min'
s3 = 'Park Dong Min'
s4 = ' Park Dong-Yun'
def process_name(name):
    name = name.replace(' ', '').replace('-', '').upper()
    return name, name.count('N')

names = [s1, s2, s3, s4]
processed = []

for name in names:
    cleaned, count = process_name(name)
    original = name.strip()
    print(f"{original}(은)는 {cleaned}(으)로 수정됨")
    processed.append((cleaned, count))
for name, count in processed:
    print(f"{name} : {count} 개의 N이 나타남")
