print("Hello World")
print("*" * 10)
x = 1
y = 2
unit_price = 3
students_count = 1000
rating = 4.99
is_published = True
course_name = "python progrmming"
print(students_count)
print(students_count * unit_price * rating)
print(len(course_name))
print(course_name[2])
first = "alameen"
last = "yussuf"
middle = "omolade"
full = f"{first} {last} {middle}"
print(full)
course = "my first python class"
print(course.upper())
print(course.lower())
print(course.rstrip())
print(course.find("cl"))
print(course.replace("first", "second"))
print("second" in course)
print("alameen" not in full)
print(10 + 3)
print(3 * 10)
print(10 - 3)
print(10 / 3)
print(10 // 3)
print(10 % 3)
print(10**3)
print(round(2.9))
print(abs(-2.9))
print(bool("false"))
print(10 >= 3)
temperatue = 35
if temperatue > 30:
    print("its warm")
    print("drink water")

print("done")

age = int(input("age: "))
if age >= 18 and age < 75:
    print(" u can apply")
else:
    print("u cant apply")

income = int(input("amount: "))
if income >= 5000:
    print("loan acknoledge")
else:
    print(" u cant borrow")
for number in range(4):
    print("send message", number + 1, (number + 1) * ".")
for x in range(5):
    for y in range(3):
        print(f"({x},{y})")
print(type(5))
print(type(range(5)))

# interable
for x in "python":
    print(x)
number = int(input("enter: "))
while number > 0:
    number = number // 2
    print(number)


def greet(first_name, last_name):
    print(f"Hi {first_name} {last_name}")
    print("welcome aboard")


greet("alameen", "yussuf")
greet("khaira", "Yussuf")


def get_greeting(name):
    return f"hi {name}"


message = get_greeting("Mosh")
print(message)

file = open("context.txt", "w")
file.write(message)


def increment(number, multiply):
    return number * multiply


print(increment(2, 3))


def multiply(x, y):
    return x - y


print(multiply(20, 10))


def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print(multiply(20, 10, 3, 9))


def user_name(**user):
    print(user["name"])


user_name(id=1, name="alameen", age=17)

message = "a"


def green(name):
    global message
    message = "b"


green("mosh")
print(message)


def add(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print(add(5, 10, 20))


def students(**user_name):
    students(score=67, name="khaira", aka="obo", info="malla")
    print(user_name["aka"])


def fizz_buzz(input):
    if input % 3 == 0:
        result = "fizz"
    else:
        result = "buzz"
    return result


print(fizz_buzz(5))

letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
]
matrix = [[0, 1], [2, 3]]
zeros = [0] * 5
combined = zeros + letters
numbers = list(range(20))
chars = list("hello world")
print(len(chars))
print(numbers)
print(combined)
print(matrix)
letters[0] = "C"
print(letters[0])
number = [1, 2, 3, 4, 5, 6, 7]
first, *other, last = number
print(first, last)
print(other)
items = [0, "a"]
index, letter = items
for letter in enumerate(letters):
    print(letter)
print(letters.count("d"))
if "d" in letter:
    print(letters.index("d"))
numbers.sort(reverse=True)
print(sorted(numbers))
print(numbers)
items = [("product2", 13), ("product3", 12), ("product4", 9), ("product5", 15)]


def sort_item(item):
    return item[1]


items.sort(key=lambda item: item[1])
print(items)


prices = []
for item in items:
    prices.append(item[1])


x = list(map(lambda item: item[1], items))
for item in x:
    print(x)

y = list(filter(lambda item: item[1] >= 10, items))
print(y)

prices = list(map(lambda item: item[1], items))
prices = [item[1] for item in items]

filtered = list(filter(lambda item: item[1] >= 10, items))
filtered = [item for item in items if item[1] >= 10]

list1 = [1, 2, 3]
list2 = [10, 20, 30]

print(list(zip("abc", list1, list2)))

browsing_session = []
browsing_session.append(1)
browsing_session.append(2)
browsing_session.append(3)
print(browsing_session)
last = browsing_session.pop()
print(last)
print(browsing_session)
print("redirect", browsing_session)
if not browsing_session:
    print("disable")

browsing_session = []
browsing_session.append(1)
browsing_session.pop()
if not browsing_session:
    browsing_session[-1]


from collections import deque

queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
queue.popleft()
print(queue)
if not queue:
    print("empty")


point = (1, 2) * 3
print(type(point))
sim = (1, 2) + (3, 4)
print(sim)
hello = tuple("hello world")
print(hello[0:2])
another = (1, 2, 3)
print(point[0:2])
x, y, z = point
if 10 in point:
    print("exists")

point[0] = 10


x = 10
y = 11

z = x
x = y
y = x
print("x", x)
print("y", y)

x, y = y, x

print("x", x)
print("y", y)

from array import array

numbrers=array("i",[1,2,3])
numbers[0] = 1.0
