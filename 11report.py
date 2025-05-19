#10-1
result1 = (123).__add__(334)
print("123 + 334 =", result1)

result2 = (123).__sub__(334)
print("123 - 334 =", result2)

result3 = (123).__mul__(334)
print("123 * 334 =", result3)


result4 = (123).__truediv__(3)
print("123 / 3 =", result4)

#10-5
a = 1
b = 1
c = 2
d = 3
e = 3

nums = {'1': [a, b], '2': [c], '3': [d, e]}

for key, lst in nums.items():
    count = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] is lst[j]:
                count += 1
    print(f"{key} : {count + 1}개" if count else f"{key} : 1개")

#10-7
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"이름은 {self.name}이고 나이는 {self.age}살입니다."


my_dog = Dog("Mango", 3)
print(my_dog)

#10-9
class Counter:
    def __init__(self, number):
        self.__number = number

    def __add__(self, other):
        result = self.__number + other.__number
        if result >= 100:
            result = 0
        return Counter(result)

    def __sub__(self, other):
        result = self.__number - other.__number
        if result <= -1:
            result = 0
        return Counter(result)

    def __str__(self):
        return f'C({self.__number})'


c1 = Counter(10)
c2 = Counter(20)
c3 = c1 + c2
c4 = c1 - c2
print('c3 =', c3)
print('c4 =', c4)

#10-11
class Student:
    def __init__(self, name, student_id):
        self.__name = name
        self.__student_id = student_id
        self.__korean_quiz = 0
        self.__math_quiz = 0
        self.__science_quiz = 0
        self.__total_score = 0

    def __str__(self):
        return (f'이름: {self.__name}, 학번: {self.__student_id}, '
                f'국어: {self.__korean_quiz}, 수학: {self.__math_quiz}, 과학: {self.__science_quiz}, '
                f'총점: {self.__total_score}')


    def get_name(self):
        return self.__name

    def get_student_id(self):
        return self.__student_id

    def get_korean_quiz(self):
        return self.__korean_quiz

    def get_math_quiz(self):
        return self.__math_quiz

    def get_science_quiz(self):
        return self.__science_quiz

    def get_total_score(self):
        return self.__total_score

    def set_korean_quiz(self, score):
        self.__korean_quiz = score

    def set_math_quiz(self, score):
        self.__math_quiz = score

    def set_science_quiz(self, score):
        self.__science_quiz = score

    def set_gwc_score(self):  
        self.__total_score = self.__korean_quiz + self.__math_quiz + self.__science_quiz



name = input("학생의 이름을 입력하세요: ")
student_id = input("학생의 학번을 입력하세요: ")
student = Student(name, student_id)

korean_quiz = int(input("국어 점수를 입력하세요: "))
math_quiz = int(input("수학 점수를 입력하세요: "))
science_quiz = int(input("과학 점수를 입력하세요: "))

student.set_korean_quiz(korean_quiz)
student.set_math_quiz(math_quiz)
student.set_science_quiz(science_quiz)
student.set_gwc_score()

print(student)

#10-13
class Rectangle:
    def __init__(self, x, y, width, height):
        self.__x = x
        self.__y = y
        self.__width = width
        self.__height = height

    def __str__(self):
        return f"Rectangle : ({self.__x}, {self.__y}, {self.__width}, {self.__height}), 면적 : {self.get_area()}"

    
    def get_x(self): return self.__x
    def get_y(self): return self.__y
    def get_width(self): return self.__width
    def get_height(self): return self.__height

    
    def set_x(self, x): self.__x = x
    def set_y(self, y): self.__y = y
    def set_width(self, width): self.__width = width
    def set_height(self, height): self.__height = height

    def get_area(self):
        return self.__width * self.__height

    def overlaps(self, r):
        
        if (self.__x + self.__width <= r.get_x() or
            r.get_x() + r.get_width() <= self.__x or
            self.__y + self.__height <= r.get_y() or
            r.get_y() + r.get_height() <= self.__y):
            return False
        return True

    def contains(self, r):
        
        return (self.__x <= r.get_x() and
                self.__y <= r.get_y() and
                self.__x + self.__width >= r.get_x() + r.get_width() and
                self.__y + self.__height >= r.get_y() + r.get_height())
