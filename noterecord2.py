

students = []

quantity = int(input("How many students do you want to register? "))

print("\n" + "="*50)
print("STUDENT REGISTRATION")
print("="*50)

for i in range(quantity):
    print(f"\n--- Student {i+1} ---")
    name = input("Enter the student's name: ")
    
    student_data = {
        "name": name,
        "subjects": [],
        "grades": []
    }
    
    num_subjects = int(input(f"How many subjects does {name} have? "))
    
    for j in range(num_subjects):
        subject = input(f"Subject {j+1}: ")
        
        
        while True:
            try:
                grade = float(input(f"Grade for {subject} (0-5): "))
                
                if grade < 0 or grade > 5:
                    print("Error: The grade must be between 0 and 5")
                    continue
                
                break
            
            except ValueError:
                print("Error: You must enter a valid number")
                continue
        
        student_data["subjects"].append(subject)
        student_data["grades"].append(grade)
    
    students.append(student_data)

print("\n" + "="*60)
print("COMPLETE STUDENT INFORMATION")
print("="*60)

best_student_name = ""  
best_average = -1       


for student in students:
    print(f"\n Name: {student['name']}")
    
    print("   Subjects and Grades:")
    for i in range(len(student['subjects'])):
        subject = student['subjects'][i]
        grade = student['grades'][i]
        print(f"      • {subject}: {grade}")
    

    total_grades = 0
    for grade in student['grades']:
        total_grades = total_grades + grade
    
    if len(student['grades']) > 0:
        average = total_grades / len(student['grades'])
    else:
        average = 0
    
    print(f"   Average: {average:.2f}")
    
    if average > best_average:
        best_average = average
        best_student_name = student['name']


print("\n" + "="*60)
print("GROUP STATISTICS")
print("="*60)

if best_student_name != "":
    print(f"\n Best student: {best_student_name}")
    print(f"   Average: {best_average:.2f}")
else:
    print("\n No students registered")


all_grades = []


for student in students:
    
    for grade in student['grades']:
        
        all_grades.append(grade)

total_all_grades = 0
for grade in all_grades:
    total_all_grades = total_all_grades + grade


if len(all_grades) > 0:
    group_average = total_all_grades / len(all_grades)
    print(f"\n Group average: {group_average:.2f}")
else:
    print("\n No grades registered")

print("\n" + "="*60)