import csv

#que:1 Create a result table 
r = []
header = ["Student ID", "Student Name", "Subject 1", "Subject 2", "Subject 3", "Subject 4", "Subject 5"]
r.append(header)

#que:2 Enter 10 student details with marks
for i in range(1,11):
    sid = i
    sname = input(f"Enter name for Student {i}: ")
    marks = []
    for j in range(5):
        submark = int(input(f"Enter marks for Subject {j+1} for Student {i}: "))
        marks.append(submark)
    r.append([sid, sname] + marks)

#que:3 Dump table into CSV file
with open("result.csv", "w", newline="") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerows(r)

#que:4 Read result.csv file and Print Total Marks and Grade of each student. Also Append Total Marks and Grade column into result.csv file.

with open("result.csv", "r") as f:
    csvreader = csv.reader(f)
    rdata = list(csvreader)

    header = rdata[0]
    header.extend(["Total Marks", "Grade"])

    for row in rdata[1:]:
        total_marks = sum(map(int, row[2:7]))
        row.extend([total_marks, "A" if total_marks >= 250 else "B" if total_marks >= 200 else "C"])

    with open("result.csv", "w", newline="") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerows(rdata)

#que:5 List out Top 3 students with percentage
with open("result.csv", "r") as f:
    csvreader = csv.reader(f)
    next(csvreader)  
    students = []

    for row in csvreader:
        sid = int(row[0])
        sname = row[1]
        total_marks = int(row[-2])
        percentage = (total_marks / 500) * 100
        students.append((sid, sname, percentage))

    top_students = sorted(students, key=lambda x: x[2], reverse=True)[:3]

    print("Top 3 Students:")
    for student in top_students:
        print(f"Student ID: {student[0]}, Name: {student[1]}, Percentage: {student[2]:.2f}%")
