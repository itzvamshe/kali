#studentss = [
#        {"name": "Alice", "age": 20, "marks": 85},
#            {"name": "Bob", "age": 19, "marks": 92},
#                {"name": "Charlie", "age": 21, "marks": 78},
#                    {"name": "David", "age": 20, "marks": 92},
#                        {"name": "Eva", "age": 18, "marks": 88}
#                        ]

students = [
    {"name": "Alice", "age": 20, "marks": 85},
    {"name": "Bob", "age": 19, "marks": 92},
    {"name": "Charlie", "age": 21, "marks": 78},
    {"name": "David", "age": 20, "marks": 92},
    {"name": "Eva", "age": 18, "marks": 88}
]

ss = sorted(students,key=lambda students:students["marks"],reverse=True)

for student in ss:
    print(student["name"], student["age"], student["marks"])
