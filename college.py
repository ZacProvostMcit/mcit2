ammount_of_student = int(input("How many student do you want to analyze: "))



for student in range(ammount_of_student):
    name = input("What is the student name: ")

    marks = {
        "Python": "",
        "Cloud Computing": "",
        "Networking": "",
        "Database": "",
        "Devops": ""
    }
    total = 0
    amount_of_grade = 0
    best_grade = 0
    lowest_grade = 101
    failed_subject = 0

    subjects = ["Python", "Cloud Computing", "Networking", "Database", "Devops"]

    for subject in subjects:
        mark = int(input(f"Enter {subject} mark: "))
        

        while int(mark) < 0 or int(mark) > 100:
            print("Invalid mark")
            mark = int(input(f"Enter {subject} mark: "))
        
            
            
        amount_of_grade += 1
        total += mark

        if mark < 50:
            failed_subject += 1


        if mark > best_grade:
            best_grade = mark

        if mark < lowest_grade:
            lowest_grade = mark
        
        marks[subject] = mark

        





    for subject, mark in marks.items():
        if mark >= 90:
            print(f"Excellent performance in {subject}")
        elif mark >= 75 and mark <= 89:
            print(f"Very good performance in {subject}")
        elif mark >= 60 and mark <= 74:
            print(f"Good performance in {subject}")
        elif mark >= 50 and mark <= 59:
             print(f"Passed {subject}")
        else:
            print("Failed")

    average = total / amount_of_grade

    
    
    print(f"Total: {total}")
    print(f"Average: {average}")
    print(f"Highest Grade: {best_grade}")
    print(f"Lowest Grade: {lowest_grade}")
    
    
    if average >= 90 and average <= 100:
        print("Grade: A+")

    elif average >= 80 and average <= 89.99:
        print("Grade: A")

    elif average >= 70 and average <= 79.99:
        print("Grade: B")

    elif average >= 60 and average <= 69.99:
        print("Grade: C")

    elif average >= 50 and average <= 59.99:
        print("Grade: D")

    else:
        print("Grade: F")
    
    print(f"Failed Subject: {failed_subject}")


    
    if failed_subject >= 2:
        print("Failed")

    elif average >= 50:
        print("Passed")

    else:
        print("Failed")

    



        



