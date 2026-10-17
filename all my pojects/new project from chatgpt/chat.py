print("my name is alameen")
print("i am learning python")
print("i want to become a software engineer")
name = "alameen"
age = 17
favourite_food = "beans"
print(name)
print(age)
print(favourite_food)
price = 250
quantity = 6
print(quantity * price)
first = "alameen"
last = "yussuf"
full = first + " " + last
print(full)
name = "alameen"
age = 17
country = "nigeria"
print(f"my name is {name}, I am {age} years old,and I live in {country}.")
word = "programming"
print(len(word))
word = "computer"
print(word[0])
print(word[1])
print(word[2])
print(word.lower())
print(word.upper())
print(word.find("g"))
sentence = "i like python"
print(sentence.replace("like python", "love java"))
course = "i love programming"
print("programming" in course)
print("programming" not in course)
print(20 + 5)
print(20 - 5)
print(20 * 5)
print(20 / 5)
print(20 // 3)
print(20 % 5)
print(2**3)
print(round(4.6))
print(round(7.2))
print(round(-10))
print(round(-3.5))
print(10 > 5)
print(3 > 8)
print(10 == 10)
print(7 < 2)
print(5 >= 5)
temperature = 50
if temperature >= 30:
    print("it's hot")
else:
    print("its not hot")
score = 60
if score >= 50 and score <= 100:
    print("allowed")
else:
    print("not allowed")
food = input("what is ur  favourite food? ")
print(f"u love {food} rigth")
password = int(input("Enter ur number: "))
print(password + 1)
for number in range(6):
    print(number)
for number in range(10):
    print("send message", number + 1)
for x in range(3):
    for y in range(2):
        print(f"({x},{y})")
number = 10
while number > 0:
    print(number)
    number = number - 1

    command = input(">")
    if command == "quit":
        break


def introduce(name, age):
    print(f"my name is{name}")
    print(f"i am age {age} old")


introduce("alameen", 17)


def student_info(name, age, course):
    print(f"my name is{name}")
    print(f"I am {age} years old")
    print(f"I am learning {course}")


student_info("alameen", 17, "python")


def calculate_age(name, birth_year):
    print(f"{name} was born in {birth_year}")


calculate_age("alameen", 2009)


def square(b):
    return b * 5


result = square(5)
print(result)


def double(c):
    return c * 2


result = double(7)
print(result)


def add(a, b):
    return a + b


result = add(10, 12)
print(result)


def wel(name):
    return f"welcom {name}"


message = wel("alameen")
print(message)


message = "welcome,alameen"

file = open("context.txt", "w")
file.write(message)
file.close()


def save_name(name):

    message = f"save your name called {name}"
    file = open("context.txt", "w")
    file.write(message)
    file.close()


save_name("alameen")


def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number

    return total


print(multiply(2, 3, 4))


def lesson(**new):
    print(f"my name is {new['name']}")
    print(f"I am {new['age']}years old")
    print(f" i am studying {new['course']}")


lesson(name="alameen", age=17, course="python")


foods = ["rice", "beans", "bread", "yam"]
print(foods[0])
print(foods[1])
print(foods[2])
print(foods[3])

languages = ["python", "javascipt", "html", "css"]
print(len(languages))

foods = ["rice", "beans"]
foods.append("yam")

foods = ["rice", "beans", "bread", "yam"]
foods.remove("yam")

languages = ["python", "javascipt", "html", "css"]


for language in languages:
    print(language)


languages = ["python", "javascript", "html", "css", "java"]
print(languages)
scores = [23, 24, 25, 26]
print(scores)
students = ["alameen", 17, 64, True]
print(students)
books = []
print(books)

print(languages[0])
print(languages[2])
print(languages[3])
print(languages[4])

print(languages[-1])
print(languages[-4])

games = ["minecraft", "fifa", "gta", "dls", "roblox"]

print(games[0])
print(games[2])
print(games[-1])
print(games[-2])

languages = ["python", "javascript", "html", "css"]

languages[2] = "react"

games = ["Minecraft", "FIFA"]
games.append("GTA")
print(games)

languages = ["Python", "JavaScript", "CSS"]
languages.insert(2, "HTML")
print(languages)

foods = []
new_foods = input("order food: ")
foods.append(new_foods)
print(foods)

games = ["Minecraft", "FIFA", "GTA", "Roblox"]

games.remove("GTA")
print(games)

languages = ["Python", "JavaScript", "HTML", "CSS"]
languages.pop(2)
print(languages)


foods = ["Rice", "Beans", "Yam", "Bread"]
del foods[0]
print(foods)

games = ["Minecraft", "FIFA", "GTA", "Roblox"]
find = games.index("FIFA")
print(find)


languages = ["Python", "JavaScript", "HTML", "CSS", "Java"]
print(languages.index("CSS"))

foods = ["Rice", "Beans", "Yam", "Bread"]
chosen_food = "Yam"
print(chosen_food)

games = ["Minecraft", "FIFA", "GTA"]

if "roblox" in games:
    print(games.index("roblox"))
else:
    print("games not in list")


games = ["Minecraft", "FIFA", "GTA", "FIFA", "Roblox", "FIFA"]

quit = games.count("FIFA")
print(quit)

numbers = [10, 20, 10, 30, 10, 40, 10]
print(numbers.count(10))

foods = ["Rice", "Beans", "Rice", "Yam", "Bread", "Rice"]
choosen_food = "Rice"

foods.count(choosen_food)
print(foods)

sales = ["Phone", "Laptop", "Phone", "Tablet", "Phone", "Laptop"]
print(sales.count("Phone"))
print(sales.count("Laptops"))

numbers = [80, 20, 50, 10, 40, 30]
numbers.sort()

scores = [45, 90, 60, 75, 30]
scores.sort(reverse=True)

games = ["Roblox", "Minecraft", "FIFA", "GTA"]
(games.sort())
print(games)

numbers = [10, 20, 30, 40, 50]

numbers.reverse()
print(numbers)

games = ["Minecraft", "FIFA", "GTA", "Roblox"]
games.reverse()
print(games)

games = ["FIFA", "GTA", "Minecraft", "Roblox", "PES"]

print(len(games))

students = ["Ahmed", "Musa", "Khaira", "Alameen"]

total_students = len(students)
print(total_students)

numbers = []
print(numbers)


students = ["alameen", "khairah", "rofiah", "musa", "bukky"]

total = len(students)
if total >= 5:
    print("we dont need student")
else:

    print("we need more student")


students = ["Ahmed", "Musa", "Alameen", "Khaira"]
print("Alameen" in students)

games = ["FIFA", "GTA", "Minecraft"]

print("PES" not in games)


games = ["FIFA", "GTA", "Minecraft", "Roblox"]

enter = input("Enter a game: ")

if enter in games:
    print("Game is available")
else:
    print("game is not available")

[20, 30, 40]

games = ["FIFA", "GTA", "Minecraft", "Roblox", "PES"]
print(games[0:3])

students = ["Ahmed", "Musa", "Alameen", "Khaira", "Rofiah"]

print(students[2:])


games = ["freefire", "GTA", "stickman", "Efootball", "DLS", "piano"]

print(games[:2])
print(games[-3:])
print(games[:-2])


numbers = [2, 4, 6, 8, 10, 12, 14, 16, 18]
print(numbers[::3])

numbers = [10, 20, 30, 40, 50, 60, 70, 80]
print(numbers[1:5:3])

games = ["FIFA", "GTA", "Minecraft", "Roblox"]

print(games[::-1])

games = ["freefire", "GTA", "stickman", "Efootball", "DLS", "piano", "motor", "ball"]
print(games[::2])
print(games[:-3:-1])
print(games[::-1])


[10, 20, 30, 40]
[10, 20, 30, 40]

first = ["FIFA", "GTA", "Minecraft"]

second = first.copy()

second.append("Roblox")

print(first)
print(second)

games = ["FIFA", "GTA", "PES"]

new_games = games.copy()

new_games.remove("GTA")

print(new_games)

students = ["Ahmed", "Musa", "Alameen"]

new_students = students[:]
new_students.append("khaira")
print(students)
print(new_students)

games = ["GTA", "piano", "ball", "run"]
backup_games = games.copy()
backup_games.append("DLS")
backup_games.remove("piano")
print(games)
print(new_games)

numbers = [5, 10, 15]

first, second, third = numbers

print(first)
print(second)
print(third)

students = ["Ahmed", "Musa", "Alameen"]

classq, classh, classt = students
print(classq)
print(classh)
print(classt)


languages = ["Python", "JavaScript", "Java"]

language1, language2, language3 = languages
print(language1)
print(language2)
print(language3)


fruits = ["Apple", "Mango", "Orange", "Banana"]

for item in fruits:
    print(item)

students = ["Ahmed", "Musa", "Alameen"]
for student in students:
    print("Hello", student)


scores = [25, 70, 45, 90, 35, 80]
for number in scores:
    if number >= 50:
        print(number)


games = ["GTA", "FIFA", "Minecraft", "PES"]

print("MY GAME COLLECTION")
for game in games:
    print(game)
    if game == "GTA":
        print("I love this game!")
print("Collection complete!")

students = ["Ahmed", "Musa", "Alameen", "Khaira"]
if "khaira " in students:
    print("Student found!")
else:
    print("student not found")


fruits = ["Apple", "Mango", "Orange", "Banana"]
print(fruits.index("Orange"))

games = ["FIFA", "GTA", "PES", "Minecraft"]
another = input("Enter a game: ")
if another in game:
    print("Game found!", game.index(another))
else:
    print("Game not found!")

numbers = [70, 20, 90, 10, 50]
another_number = sorted(numbers)
print(another_number)

games = ["Minecraft", "FIFA", "GTA", "PES"]
print(games.sort(reverse=True))

banga = [45, 10, 80, 25, 60]
another_banga = sorted(banga)
print(another_banga)
print(banga)

languages = ("Python", "JavaScript", "Java")

print(languages[0])
print(languages[-1])

30
40
4

phones = ("Samsung", "iPhone", "Infinix", "Tecno")
normal = list(phones)
normal[1] = "Google Pixel"
normal[-1] = "Nokia"
phones = tuple(normal)
print(phones)

laptop = {"brand": "HP", "RAM": "8GB", "storage": "512GB"}

print(laptop["brand"])
print(laptop["RAM"])

phone = {"brand": "Samsung", "color": "Black"}

phone["price"] = 150000

student = {"name": "Musa", "age": 16, "language": "Java"}

student["age"] = 17
student["language"] = "python"
student["country"] = "Nigeria"

laptop = {"brand": "HP", "RAM": "8GB", "storage": "512GB"}

print(laptop.get("brand"))
print(laptop.get("price", "unknown"))
print(laptop.keys())
print(laptop.values())

laptop = {"brand": "HP", "RAM": "8GB", "storage": "512GB", "color": "Silver"}

laptop.pop("RAM")
print(laptop)
del laptop["color"]
print(laptop)
laptop.clear()
print(laptop)

phone = {"brand": "Samsung", "color": "Black", "price": 150000}
for key in phone:
    print(key)
for values in phone:
    print(values)
for key, values in phone.items():
    print(key, values)

phone = {"brand": "Samsung", "color": "Black", "price": 150000}

if "brand" in phone:
    print("Brand found")
else:
    print("Brand not found")

if "battery" in phone:
    print("Battery found")
else:
    print("Battery not found")

languages = {"Python", "Java", "Python", "JavaScript", "Java"}
print(languages)


students = ["Musa", "Alameen", "Musa", "Khaira"]
names = set(students)
students = list(names)
print(students)

football_players = {"Ronaldo", "Messi", "Salah", "Mbappe"}
basketball_players = {"LeBron", "Curry", "Messi", "Salah"}

print(football_players | basketball_players)

numbers = [3, 5, 7]

another = [number**2 for number in numbers]
print(another)


stack = []
stack.append("Musa")
stack.append("Salah")
stack.append("Yusuf")

stack.pop()
print(stack)

name = []
name.append("Ali")
name.append("Umar")
name.append("Usman")

pname = name.popleft()
print(pname)

try:
    name = input("Enter your name: ")
    print("thanks you", name, "can enter")

except ValueError:
    print("please anter a name")

except IndexError:
    print("enter ur name not number")

print("====== divisional claculator ======".upper())

try:
    first = int(input("Enter your first number: "))
    second = int(input("Enter your second number: "))
    total = first / second
    print("result = ", total)
except ValueError:
    print("Please enter valid numbers!")
except ZeroDivisionError:
    print("You cannot divide by zero!")
finally:
    print("the calculations has ended")


class car:
    pass


car1 = car()
car2 = car()
car3 = car()


class laptop:
    pass


laptop1 = laptop()
laptop2 = laptop()
laptop3 = laptop1
print(laptop3 is laptop1)
print(laptop1 is laptop2)


class car:
    def __init__(self, brand):
        self.brand = brand


car1 = car("toyota")
car2 = car("honda")
print(car1.brand)
print(car2.brand)


class student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


student1 = student("alameen", 17)
print(student1.name)
print(student1.age)


class Dog:
    def __init__(self, name, age, bork):
        self.name = name
        self.age = age
        self.bork = bork

    def bark(self):
        print(f"{self.name} is {self.age} years old and says {self.bork}!")


dog1 = Dog("bingo", 4, "woof")
dog2 = Dog("bunny", 2, "awooooo")

dog1.bark()
dog2.bark()


class BankAccount:
    def __init__(
        self,
        owner,
        balance,
    ):
        self.owner = owner
        self.balance = balance

    def show_balance(self):
        print(f"{self.owner}'s account balance is #{self.balance}")

    def deposit(self, amount):

        self.balance = self.balance + amount


first = BankAccount("alameen", 50000)
second = BankAccount("ahmed", 80000)

first.show_balance()
first.deposit()
second.show_balance()


class Pet:
    def __init__(self, name, animal, age):
        self.name = name
        self.animal = animal
        self.age = age

    def introduce(self):
        print(
            f"My name is {self.name}. I am a {self.animal}, and I am {self.age} years old."
        )


pet1 = Pet("hurayra", "cat", 4)
pet2 = Pet("zaira", "chicken", 3)

pet1.introduce()
pet2.introduce()


class GameCharacter:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def take_damage(self):
        self.health -= 10

    def show_health(self):
        print(f"Brother {self.name} your current health is {self.health}")


patience1 = GameCharacter("alameen", 100)
patience2 = GameCharacter("alameen", 100)

patience1.show_health()
patience1.take_damage()
patience2.show_health()
patience2.take_damage()


class Student:
    student_count = 0
    school="Fajr center"
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.student_count+= 1
        

    def about_student(self):
        print(f"your name is {self.name}.You are {self.age} years old, You are a bonafied student of {self.school} ")
        
    @classmethod
    def amount_student(cls):
        print(cls.student_count)

student1 = Student("Alameen",15)
student2 = Student("khaira",16)
student3 = Student("rofia",17)
student4 = Student("maryam",18)

student1.about_student
student1.amount_student
student2.about_student
student2.amount_student
student3.about_student
student3.amount_student
student4.about_student
student4.amount_student
student.amount_student


class Phone:
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price

    def __str__(self):
        return f"My phone is {self.brand} and it costs ₦{self.price}."
phone1 = Phone("samsung",15000)

print(phone1)


class Person:
    def __init__(self,name):
        self.name = name
    def introduce(self):
        print(f"i am a {self.name}")

class Student(Person)    :
    def study(self):
        super().introduce()
        print("I am studying Python")

student1 = Student("alameen")

student1.introduce()
student1.study()

class Person:
    def __init__(self,name):
        self.name = name


class Student(Person):
    def __init__(self, name,age):
        super().__init__(name)
        self.age = age

student1 = Student("Alameen",17)

print(student1.name)
print(student1.age)

class Writer:
    def write(self):
    
        print("I can write.")

class Singer:
    def sing(self):
        print("I can sing.")
        
class Artist(Writer,Singer):
    pass
artist1 = Artist()
artist1.write()
artist1.sing()
