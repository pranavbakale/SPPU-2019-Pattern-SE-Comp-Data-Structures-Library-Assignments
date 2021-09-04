# Assignment No. 2 : In a second year computer engineering class, group A students play cricket, group B students play
#                    badminton and group C students play football. Write a python program using functions to compute following:
#                    a) List of students who play both cricket and badminton.
#                    b) List of students who play either cricket or badminton but not both.
#                    c) Number of students who play neither cricket nor badminton.
#                    d) Number of students who play cricket and football but not badminton.
#                    (NOTE : While realising the group, duplicate entries should be avoided. Do not use SET built-in functions)



def remove_duplicate(dup):
    student_list = []
    for a in dup:
        if a not in student_list:
            student_list.append(a)
    return student_list


def intersection(student_list1, student_list2):
    intersection_list = []
    for b in student_list1:
        if b in student_list2:
            intersection_list.append(b)
    return intersection_list


def union(students_list1, students_list2):
    union_list = students_list1.copy()
    for c in students_list2:
        if c not in union_list:
            union_list.append(c)
    return union_list


def difference(students_list1, students_list2):
    difference_list = []
    for d in students_list1:
        if d not in students_list2:
            difference_list.append(d)
    return difference_list


def difference_compliment(students_list1, students_list2):
    diff1 = difference(students_list1, students_list2)
    diff2 = difference(students_list2, students_list1)
    differenceCompliment_list = union(diff1, diff2)
    return differenceCompliment_list


def both_cb(students_list1, students_list2):
    both_cbList = intersection(students_list1, students_list2)
    return both_cbList


def either_cb(students_list1, students_list2):
    either_cbList = difference_compliment(students_list1, students_list2)
    return either_cbList


def neither_cb(students_list1, students_list2, students_list3):
    neither_cbList = difference(students_list1, union(students_list2, students_list3))
    return len(neither_cbList)


def cf_nob(students_list1, students_list2, students_list3):
    cf_nobList = difference(intersection(students_list1, students_list2), students_list3)
    return len(cf_nobList)


se_computer = []
seStudentsNo = int(input("Enter the number of students in SE Computer :"))
print("Enter the name of the", seStudentsNo, "students in SE Computer :")
for i in range(0, seStudentsNo):
    students = input()
    se_computer.append(students)
print("The list of students in SE Computer is :", se_computer)


cricket = []
cricketNo = int(input("\nEnter the number of students who play Cricket :"))
print("Enter the name of the", cricketNo, "students who play Cricket :")
for j in range(0, cricketNo):
    cricket_students = input()
    cricket.append(cricket_students)
print("The original list of students playing cricket is :", cricket)
cricket = remove_duplicate(cricket)
print("The list of students playing Cricket after removing duplicates is :", cricket)


football = []
footballNo = int(input("\nEnter the number of the students who play Football :"))
print("Enter the name of the", footballNo, "students who play Football :")
for k in range(0, footballNo):
    football_students = input()
    football.append(football_students)
print("The original list of students playing Football is :", football)
football = remove_duplicate(football)
print("The list of students playing Football after removing duplicates is :", football)


badminton = []
badmintonNo = int(input("\nEnter the number of the students who play Badminton :"))
print("Enter the name of the", badmintonNo, "students who play Badminton :")
for k in range(0, badmintonNo):
    badminton_students = input()
    badminton.append(badminton_students)
print("The original list of students playing Badminton is :", badminton)
badminton = remove_duplicate(badminton)
print("The list of students playing Badminton after removing duplicates is :", badminton)


flag = 1;
while flag == 1:
    print("\nSelect any option you want :")
    print("1] List of students who play both Cricket and Badminton.")
    print("2] List of students who play either Cricket or Badminton but not both.")
    print("3] Number of students who play neither Cricket nor Badminton.")
    print("4] Number of students who play Cricket and Football but not Badminton.")
    print("5] Exit.")
    option = int(input("\nEnter Option :"))

    if option == 1:
        print("\nList of students who play both Cricket and Badminton :", both_cb(cricket, badminton))
        con = input("\nDo you want to close (y/n) :")
        if con == "y":
            break
        else:
            flag = 1

    elif option == 2:
        print("\nList of students who play either Cricket or Badminton but not both :", either_cb(cricket, badminton))
        con = input("\nDo you want to close (y/n) :")
        if con == "y":
            break
        else:
            flag = 1

    elif option == 3:
        print("\nNumber of students who play neither Cricket nor Badminton :", neither_cb(se_computer, cricket, badminton))
        con = input("\nDo you want to close (y/n) :")
        if con == "y":
            break
        else:
            flag = 1

    elif option == 4:
        print("\nNumber of students who play Cricket and Football but not Badminton :", cf_nob(cricket, football, badminton))
        con = input("\nDo you want to close (y/n) :")
        if con == "y":
            break
        else:
            flag = 1

    elif option == 5:
        flag = 0

    else:
        print("\nPlease select correct option !!")
        con = input("\nDo you want to close (y/n) :")
        if con == "y":
            break
        else:
            flag = 1
