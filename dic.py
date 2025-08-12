students = {"alice": 85, "bob": 92, "charlie": 78, "diana": 88}

name = input("Enter the student's name: ").strip().lower()

print(students.get(name, f"Student '{name}' not found."))
