print("====== STUDENT LIST MANAGER ======")
students=["alameen","yussuf","musa","abdullah","khaira",]
while True:
    
    add=print("1. Add student")
    view=print("2. view students")
    remove= print("3. Remove student")
    quit=print("4. Quit")

    any = int(input("enter the number of the option u want: "))
    if any == 1:
        add_name = input("Enter name of student u want to add: ")
        add_student=students.append(add_name)
        print("student added to the list")
    elif any == 2:
        for student in students:
            print(student)
    elif any == 3:
        remove_student=input("enter students you want to remove: ")
        if remove_student in students:
            students.remove(remove_student)
            print("student removal successfull")
        else:
            print("student not found")
    elif any == 4:
        print("bye for now")
    break
    
else:
    print
    