#Se desarrollará un pequeño sistema que permita registrar estudiantes, sus materias y las notas obtenidas.
#El sistema también debe calcular el promedio de cada estudiante y mostrar información general del grupo.
#Este proyecto se desarrollará usando una metodología ágil inspirada en Scrum, con un sprint de 3 días.
#Día 1 — Registro de estudiantes
# Objetivo del sprint
#Permitir registrar estudiantes en el sistema.
#Tareas
#Crear estructura para guardar estudiantes
#Permitir ingresar varios estudiantes
#Mostrar lista de estudiantes registrados

students = []

quantity = int(input("How many students do you want to register? "))

for i in range(quantity):
    print(f"\n--- Student {i+1} ---")
    name = input("Enter the name of the student: ")
    
    student_data = {
        "name": name,
        "subjects": [],
        "grades": []
    }
    
    num_subjects = int(input(f"How many subjects does {name} have? "))
    
    for j in range(num_subjects):
        subject = input(f"Subject {j+1}: ")
        grade = float(input(f"Grade for {subject}: "))
        
        student_data["subjects"].append(subject)
        student_data["grades"].append(grade)
    
    students.append(student_data)

print("\n" + "="*50)
print("LIST OF REGISTERED STUDENTS")
print("="*50)

for student in students:
    print(f"\nName: {student['name']}")
    print("Subjects and Grades:")
    
    for i in range(len(student['subjects'])):
        subject = student['subjects'][i]
        grade = student['grades'][i]
        print(f"  - {subject}: {grade}")
    