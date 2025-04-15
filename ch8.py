#8.1
from datetime import date

start_date = date(2019, 2, 14)
today = date.today()
delta = today - start_date

print(f"춘향이와 몽통이의 연애 시작일 : {start_date.year}년 {start_date.month}월 {start_date.day}일")
print(f"연애 시작일로부터 경과한 날짜 : {delta.days}일")

from datetime import datetime, timedelta

start_date = datetime(2019, 2, 14)
print(f"춘향이와 몽통이의 연애 시작일 : {start_date.year}년 {start_date.month}월 {start_date.day}일")

anniversaries = {
    100: start_date + timedelta(days=100),
    200: start_date + timedelta(days=200),
    500: start_date + timedelta(days=500),
    1000: start_date + timedelta(days=1000)
}

for days, anniversary in anniversaries.items():
    print(f"{days}일 기념일 : {anniversary.year}년 {anniversary.month}월 {anniversary.day}일")
#8.5
import math

for angle in range(0, 181, 10):
    rad = math.radians(angle)
    sin_val = math.sin(rad)
    cos_val = math.cos(rad)
    tan_val = math.tan(rad)
    
print(f"sin({angle:3}) = {sin_val:.3f}, cos({angle:3}) = {cos_val:.3f}, tan({angle:3}) = {tan_val:.3f}")

#8.9
import random

def number_guessing_game():
    x = random.randint(1, 20)
    attempts = 0
    
    while True:
        guess = int(input("1~20까지의 숫자를 입력하세요: "))
        attempts += 1
        
        if guess < x:
            print(f"{guess} 보다 큽니다!")
        elif guess > x:
            print(f"{guess} 보다 작습니다!")
        else:
            print("정답입니다!")
            
            if attempts <= 3:
                print(f"{attempts}번만에 맞춘 당신은 천재!")
            elif 4 <= attempts <= 6:
                print(f"{attempts}번만에 맞추셨네요. 괜찮아요^^")
            else:
                print(f"{attempts}번만에 맞추다니 쩝쩝...")
            break

number_guessing_game()
