while True:
    print("====== STUDENT MANAGEMENT SYSTEM =====")
    print("1.Add student")
    print("2.View student")
    print("3.Search student")
    print("4. remove student")
    print("5.Calculate average score")
    print("6.view student who passed")
    print("7. Exit")

    students = ["alameen"]

    choice = int(input("Enter your choice: "))
    print("You selected option", choice)
    try:
        if choice == 1:
            student_name = input("Enter student you want to add: ")
            students.append(student_name)
            print("The student has been added")

        elif choice == 2:
            print("The students are: ")
            for student in students:
                print(student)
        elif choice == 3:
            search_name = input("Enter student you want to search: ")
            if search_name in students:
                print(search_name, "is in the list of student")
        elif choice == 4:
            remove_student = input("Enter the student you want to remove: ")
            if remove_student in students:
                students.remove(remove_student)
                print("student has been removed from the list")
        elif choice == 5:

            print("Enter student 1st term 2nd term and third term score: ")

            first = int(input("1st term: "))
            second = int(input("2st term: "))
            third = int(input("3st term: "))
            total = first + second + third 
            average=total / 3
            print ("Your Total : ",total)
            print ("Your average : ",average)

            if total >= 50 and total <= 100:
                print("You are promoted to next class")
            else:
                print("you are repeating the current class")
        elif choice == 7:

            break
    except ValueError:
        print("Enter a valid number in the option")
    finally:
        print("score checked finished!")