student = {
        "name" : "John",
        "age" : 25,
        "anime" : "Monster",
        "siblings" : "Sister"
        }

print(student)
print(student.keys())
print(student.values())
print(student.items())

for k,v in student.items():
    print(k,v)


# student["name"] = "monster" to update existing key and value
# student.update({"name":"monster","age":30})


