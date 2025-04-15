#7.1
price = {'김밥': 5000, '아이스크림': 3000, '떡볶이': 2000}
price['김밥'] 
price['김밥'] = 6000
price 
price.values() 
price.keys() 
print(f"이 식당의 메뉴 개수는 {len(price)} 개 입니다.")  
#7.5
t = (10, 20, 30, 40)
print(t[0])  
print(t[0:2]) 
print(t[1:1]) 
print(t[:3]) 
print(t[1::2]) 
print(t[:-1])
#7.9
tup = (1, 2, 5, 4, 3, 2, 1, 4, 7, 8, 9, 9, 3, 7, 3)
unique_tup = tuple(set(tup)) 
print(f"중복 제거 튜플: {unique_tup}")
#7.13
def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]  
    return lst
original_list = [5, 6, 3, 9, 2, 12, 3, 8, 7]
sorted_list = bubble_sort(original_list.copy())
print(f"정렬된 결과는 = {sorted_list}")

#7.17
population_A = (100, 150, 230, 120, 180, 100, 140, 95, 81, 21, 4)
population_B = (300, 420, 530, 420, 400, 300, 40, 5, 1, 1, 1)

votes_A = sum(population_A[2:])
votes_B = sum(population_B[2:])
print(f"마을 A와 B에 보낼 투표용지의 개수는 각각 {votes_A} 장과 {votes_B} 장입니다.")

elderly_A = sum(population_A[7:]) / sum(population_A)
elderly_B = sum(population_B[7:]) / sum(population_B)
print(f"마을 A와 B의 고령화 정도는 각각 {elderly_A:.3f}와 {elderly_B:.3f}입니다.")
#7.21
def is_palindrome(s):
    s = ''.join(c.lower() for c in s if c.isalpha())
    return s == s[::-1]

input_str = input("문자열을 입력하시오: ")
if is_palindrome(input_str):
    print("회문입니다.")
else:
    print("회문이 아닙니다.")
