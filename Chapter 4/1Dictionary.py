info = {
    "name" : "apnacollege",
    "learning" : ["python", "C", "C++", "Java"],
    "topics" : ("dict", "set"),
    "age" : 24,
    "is_adult" : True,
    "marks" : 94.5
}

print(info["name"])
print(info["learning"])
print(info["topics"])
print(info["age"])

info["name"] = "Priya" #change existing value
info["surname"] = "Vats" #add new key:value
print(info)

null_dict = {}
null_dict["name"] = "Priya"
print(null_dict)
