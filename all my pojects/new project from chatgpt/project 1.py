print("====== STUDENT SYSTEM ======")

name=input("Enter your name: ")
age=int(input("Enter your age: "))
country=input("Enter your country: ")
course=input("Enter your course: ")
score=int(input("Enter your score: "))

print("====== STUDENT INFORMATION ======")
print(name)

if age >=7 and age <=20:
    print (age)
else:
    print("you are not a candidate")
print(country)
print(course)
print(score)
if score >= 50 and score <=100:
    print("result: passed")
else:
    print("result: failed")
