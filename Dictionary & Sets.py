student = {
    "name": "pallab",
    "city": "nagaon",
    "state": "assam",
    "country": "india"
}
print(type(student))
print(student["name"])

print(student["city"]) 
student["country"] = "canada"    #for change value in dictionary !!
print(student["country"])
student["favSubject"]= "Maths"   # add new key 
print(student)

student.pop("state")
print(student) 

print(student.keys())     #for know all keys