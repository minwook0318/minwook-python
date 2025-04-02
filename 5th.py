list_ex = [10, 20, 30, 40, 50, 60, 70]
high=5
low= 3

print(list_ex[low])       
print(list_ex[low + 2])    
print(list_ex[high - low]) 
print(list_ex[low - high]) 
print(list_ex[-1])         
print(list_ex[-low])       
print(list_ex[2 * 3])      
print(list_ex[2] * 3)      
print(list_ex[5 % 4])      
print(len(list_ex))

#6.3
list1 = [3, 5, 7]
list2 = [2, 3, 4, 5, 6]

for x in list1:
    for y in list2:
        if isinstance(y, int):
            print(f"{x} * {y} = {x * y}")

#6.5
list1 = ['I like', 'I love']
list2 = ['pancakes.', 'kiwi juice.', 'espresso.']

for phrase in list1:
    for item in list2:
        print(f"{phrase} {item}")

#6.7
n_list = [10, 20, 30, 50, 60]
total = 0

for num in n_list:
    total += num

print(f"리스트 원소들: {n_list}")
print(f"리스트 원소들의 합: {total}")

#6.9
n_list = [10, 20, 30, 50, 60]
max_val = n_list[0]

for num in n_list[1:]:
    if num > max_val:
        max_val = num

print(f"리스트 원소들: {n_list}")
print(f"리스트 원소들 중 최댓값: {max_val}")

#6.11
numbers = list(map(int, input("5개의 수를 입력하세요: ").split()))
print(f"합: {sum(numbers)}")
print(f"평균: {sum(numbers)/len(numbers)}")
print(f"최댓값: {max(numbers)}")
print(f"최솟값: {min(numbers)}")

#6.13
import math

n = int(input("n을 입력하세요: "))
data = list(map(float, input(f"{n}개의 수를 입력하세요: ").split()))
mean = sum(data) / n
variance = sum((x - mean) ** 2 for x in data) / n
std_dev = math.sqrt(variance)

print(f"합: {sum(data)}")
print(f"평균: {mean:.2f}")
print(f"표준편차: {std_dev:.2f}")

#6.15
greet = 'Have a beautiful day.'
print(greet[:4])    
print(greet[7:16]) 
print(greet[-4:-1])

#6.17
animals = ['dog', 'cat', 'tiger', 'lion']
print(f"animals = {animals}")

animals.append(animals.pop(0))
print(f"animals = {animals}")

for animal in animals:
    print(f"I love {animal}.")

#6.19
s_list = ['abc', 'bcd', 'abc', 'abba', 'cddc', 'opq', 'opq']
new_s_list = []

for item in s_list:
    if item not in new_s_list:
        new_s_list.append(item)

print(f"new_s_list = {new_s_list}")


#6.21
src = 'a2b3c6a2c3f1g1'
output = ''
i = 0

while i < len(src):
    char = src[i]
    count = int(src[i+1])
    output += char * count
    i += 2

print(f"output = {output}")

#6.23
def how_many_persons(person_list):
    return len(person_list) // 5

def compute_average_age(person_list):
    ages = person_list[1::5]
    return sum(ages) / len(ages)

def count_males_females(person_list):
    genders = person_list[2::5] 
    return genders.count(1), genders.count(0)

def display_persons(person_list):
    for i in range(0, len(person_list), 5):
        print(person_list[i:i+5])
