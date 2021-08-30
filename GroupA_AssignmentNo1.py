/*
Assignment Number 1 : Write a python program to store marks stored in subject "Fundamentals of Data Structure" by
                      N students in the class. Write functions to compute following:
                        1. The average score of the class.
                        2. Highest score and lowest score of the class.
                        3. Count of students who were absent for the test.
                        4. Display mark with highest frequency.
*/



n = int(input("Enter number of students :"))
marks_list = []
print("\nNote : Please enter -1 if Student is Absent :\n")
count = 0
for i in range(n):
    m = int(input("Enter marks :"))
    if m == -1:
        count += 1
        continue
    else:
        marks_list.append(m)

avg = sum(marks_list) / len(marks_list)
marks_list.sort()

x = 0
res = marks_list[0]
for k in marks_list:
    freq = marks_list.count(k)
    if freq > x:
        x = freq
        res = k

print("\nAverage Score of Class is :", avg)
print("\nHighest Score of Class is :", marks_list[-1])
print("\nLowest Score of Class is :", marks_list[0])
print("\nNo of Absent Students :", count)
print("\nMost Frequent Marks is :", res)
