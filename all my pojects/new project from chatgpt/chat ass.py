print("====== STUDENT SYSTEM ======")
while True:
    name = input("Enter student name or(quit):")
    if name == "quit":
        break
    

age = int(input("Enter age: "))
score = int(input("Enter score:"))
print("student:", name)
if age >= 7 and age <= 20:
    print("age", age)
else:
    print("u are not a candidate")
print("score", score)

if score >= 50 and score <= 100:
    print("passed")
else:
    print("failed")


