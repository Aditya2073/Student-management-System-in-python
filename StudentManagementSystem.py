import os

def enter_data():
    global student_roll
    print("Enter Students roll no", end=" ")
    student_roll = int(input())
    f = open(str(student_roll), "w")
    f.write("|--------------------------------------------|")
    student_name = input("Enter Students name: ")
    f.write('\n Students Name: ' + student_name)
    student_class = input("Enter Students class: ")
    f.write('\n Students Class: ' + student_class)
    student_percentage = int(input("Enter Students percentage: "))
    f.write('\n Students Percentage: ' + str(student_percentage))
    f.write('\n Students Roll No: ' + str(student_roll))
    f.write("\n|--------------------------------------------|")
    f.close()

def search_data():
    print('Enter the roll no you want to search or to exit to main menu type "exit":', end=" ")
    search_rollno = input()
    if os.path.isfile(search_rollno):
        f = open(search_rollno, "r")
        print(f.read())
        f.close()
    elif search_rollno == "exit":
        Stud_Mng_Sys()
    else:
        print("Enter a valid roll no...")
        search_data()


def update_data():
    print('Enter the roll no you want to update or to exit to main menu type "exit":', end=" ")
    up = int(input())
    if os.path.isfile(str(up)):
        f = open(str(up), "w")
        f.write("|--------------------------------------------|")
        student_name = input("Enter Students name: ")
        f.write('\n Students Name: ' + student_name)
        student_class = input("Enter Students class: ")
        f.write('\n Students Class: ' + student_class)
        student_percentage = int(input("Enter Students percentage: "))
        f.write('\n Students Percentage: ' + str(student_percentage))
        student_new_roll = int(input("Enter Students Roll: "))
        f.write('\n Students Roll No: ' + str(student_new_roll))
        f.write("\n|--------------------------------------------|")
        f.close()
        os.rename(str(up), str(student_new_roll))
    elif up == "exit":
        Stud_Mng_Sys()
    else:
        print("Enter a valid roll no...")
        update_data()


def Stud_Mng_Sys():
    print("|--------------------------------------------|")
    print("| 1 Enter Data                               |")
    print("| 2 search data                              |")
    print("| 3 update data                              |")
    print("| 4 Exit                                     |")
    print("|--------------------------------------------|")
    ch = int(input("|Enter Your Choice: "))
    if ch == 1:
        enter_data()
        os.system('cls')
        Stud_Mng_Sys()
    elif ch == 2:
        search_data()
        Stud_Mng_Sys()
    elif ch == 3:
        update_data()
        os.system('cls')
        Stud_Mng_Sys()
    elif ch == 4:
        print("\n Thank You")
        exit()
    else:
        print("Enter a correct choice")
        Stud_Mng_Sys()


Stud_Mng_Sys()
